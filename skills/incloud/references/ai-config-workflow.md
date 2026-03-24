# AI 配置工作流参考

本文档指导 AI 工具（如 Claude Code）通过 incloud CLI 完成设备配置的完整流程：发现 Schema → 理解约束 → 构造 JSON → 校验 → 写入。

## 完整工作流

```bash
# 1. 了解配置间的依赖关系（如有）
incloud device config schema overview --device <id>

# 2. 发现有哪些可配置项
incloud device config schema list --device <id>

# 3. 获取目标配置的 JSON Schema 定义
incloud device config schema get --device <id> <json-key>

# 4. 查看设备当前配置（修改/删除前必做）
incloud device config get <id> -o yaml

# 5. （根据 Schema 构造配置 JSON）

# 6. 写入前校验
incloud device config schema validate --device <id> --key <json-key> --payload '<json>'

# 7. 写入配置
incloud device config update <id> --payload '<json>'

# 8. 验证结果
incloud device config get <id> -o yaml
```

## Schema 命令详解

### 查看配置概览

```bash
incloud device config schema overview --device <id>
# 或直接指定产品/版本
incloud device config schema overview --product MR805 --version 2.0.4-alpha.8
```

输出 markdown 格式的配置依赖规则。不是所有产品版本都有概览数据。

### 列出配置 Schema

```bash
incloud device config schema list --device <id>
incloud device config schema list --product MR805 --version 2.0.4-alpha.8
# 按名称正则过滤
incloud device config schema list --device <id> --name "DNS|WiFi"
```

返回所有配置项的摘要（name、jsonKeys、description），约 20-30 条。

### 获取单个 Schema

```bash
incloud device config schema get --device <id> dns -o json
```

返回完整的 JSON Schema（draft-07），包含字段类型、枚举值、required 字段、格式约束等。**构造配置 JSON 前必须先读 Schema。**

### 校验配置 JSON

```bash
# 从命令行传入
incloud device config schema validate --device <id> --key dns --payload '{"dns":{"dns1":"8.8.8.8"}}'

# 从文件传入
incloud device config schema validate --device <id> --key dns --file config.json
```

- 校验通过：stderr 输出 `Validation passed.`，exit code 0
- 校验失败：输出具体错误路径和原因，exit code 1

### 参数说明

`--device` 与 `--product`/`--version` 互斥：
- `--device <id>` — 自动从设备推断产品和固件版本
- `--product <code> --version <ver>` — 直接指定，跳过设备查询

注意：`--device` 使用的是设备当前固件版本，而 config-documents 数据按固件版本入库。如果该版本没有对应的 Schema 数据，list 会返回空结果。此时需要用 `--product`/`--version` 指定有数据的版本。

## 配置写入语义

`incloud device config update` 使用 **JSON Merge Patch** 语义，不同数据类型的处理规则不同。

### 对象类型（Object）

**增量合并**——只发送要变更的字段，后端自动合并。

```bash
# 只改 dns1，dns2 保持不变
incloud device config update <id> --payload '{"dns":{"dns1":"223.5.5.5"}}'
```

修改时需注意：如果 Schema 中该对象有 `required` 字段，payload 中需包含这些 required 字段（即使值不变），否则可能校验失败。

### 数组类型（Array）

**全量替换**——必须发送完整数组，不是增量追加。

```bash
# 错误：只发新增项（会丢失原有项）
incloud device config update <id> --payload '{"items":[{"name":"new"}]}'

# 正确：先 GET 获取当前数组，追加新项后发送完整数组
# 假设当前有 [A, B]，要加 C：
incloud device config update <id> --payload '{"items":[A, B, {"name":"new"}]}'
```

操作步骤：
1. `incloud device config get <id>` 获取当前配置
2. 从中提取目标数组
3. 追加/修改/删除数组元素
4. 发送完整数组

### 删除配置

对象的键删除：将值设为 `null`。

```bash
# 删除 dns 配置
incloud device config update <id> --payload '{"dns":null}'
```

数组中删除元素：发送不含该元素的完整数组。

### 关键 ID 格式

部分配置（如端口映射、VPN 隧道、WiFi SSID）使用 16 位十六进制 ID 作为 key：

```json
{
  "port_mapping": {
    "0000a1b2c3d4e5f6": { "name": "Web Server", ... }
  }
}
```

新增条目时需生成此格式的 ID（前 4 位为序号，后 12 位随机），具体格式见各 Schema 的 `patternProperties`。

## 依赖检查

修改或删除配置前，需考虑配置间的依赖关系：

- **添加前检查前置依赖**：如添加防火墙规则引用了某个接口，该接口配置必须已存在
- **删除前检查反向依赖**：如删除某接口配置前，检查是否有路由、防火墙规则引用它
- **IPPT 互斥**：IP 直通（IPPT）启用时，不能配置 L2TP VPN、MAC 过滤等功能

概览文档（`schema overview`）中会描述这些依赖关系。无概览时，根据 Schema 的 description 和 title 推断。

## 常见场景

### 场景 1：配置 DNS

```bash
incloud device config schema get -d <id> dns -o json    # 1. 查看 Schema
incloud device config get <id> -o yaml                   # 2. 查看当前配置
# 3. 构造并校验
incloud device config schema validate -d <id> --key dns \
  --payload '{"dns":{"dns1":"223.5.5.5","dns2":"114.114.114.114"}}'
# 4. 写入
incloud device config update <id> \
  --payload '{"dns":{"dns1":"223.5.5.5","dns2":"114.114.114.114"}}'
```

### 场景 2：添加端口映射规则

```bash
incloud device config schema get -d <id> port_mapping -o json  # 1. 查看 Schema
incloud device config get <id> -o yaml                         # 2. 查看当前端口映射
# 3. 构造 JSON（注意 ID 格式和 required 字段如 fwd_mode）
# 4. 校验
incloud device config schema validate -d <id> --key port_mapping \
  --payload '{"port_mapping":{"0000a1b2c3d4e5f6":{"name":"SSH","enabled":true,"fwd_mode":"external","protocol":"tcp","external_port":"2222","ip":"192.168.1.1","internal_port":"22"}}}'
# 5. 写入
incloud device config update <id> --payload '...'
```

### 场景 3：修改 WiFi 密码

```bash
incloud device config schema get -d <id> wlan_ap -o json  # 1. 查看 WiFi Schema
incloud device config get <id> -o yaml                     # 2. 找到目标 SSID 的 key ID
# 3. 只修改 key 字段，但必须包含 required 字段（mode, enabled, ssid）
incloud device config update <id> \
  --payload '{"wlan_ap":{"00005b68f7e4ece6":{"mode":"ap","enabled":true,"ssid":"MyWiFi","key":"newpassword123"}}}'
```

## 注意事项

1. **写入前必须先查 Schema**：不要凭记忆或猜测构造配置 JSON，字段名和结构因产品型号而异
2. **修改前必须先 GET**：获取当前配置状态，避免覆盖或遗漏
3. **校验是安全网**：`schema validate` 只做 JSON Schema 语法校验，不检查业务逻辑（如依赖关系）。校验通过不代表配置一定合理
4. **Version 匹配**：config-documents 按固件版本存储。设备当前固件版本可能没有对应的 Schema 数据，需要找最近的可用版本
5. **设备必须在线**：配置写入需要设备在线。离线设备的配置变更会在设备上线后自动下发

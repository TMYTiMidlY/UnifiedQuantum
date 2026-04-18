# 配置管理 (`uniq config`)

管理云平台的 API 密钥和配置。

## 初始化配置

```bash
# 创建默认配置文件
uniq config init
```

配置文件位置：`~/.uniq/uniq.yml`

## 设置配置项

```bash
# 设置平台 Token
uniq config set originq.token YOUR_TOKEN
uniq config set quafu.token YOUR_TOKEN
uniq config set ibm.token YOUR_TOKEN

# 在指定 profile 下设置
uniq config set originq.token YOUR_TOKEN --profile production
```

## 查看配置

```bash
# 查看特定平台配置
uniq config get originq

# 列出所有平台配置状态
uniq config list

# 以 JSON 格式输出
uniq config list --format json
```

## 验证配置

```bash
# 验证当前配置是否有效
uniq config validate
```

## 配置 Profile 管理

```bash
# 列出所有 profile
uniq config profile list

# 切换 profile
uniq config profile use production

# 创建新 profile
uniq config profile create testing
```

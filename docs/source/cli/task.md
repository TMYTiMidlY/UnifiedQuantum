# 任务管理 (`uniq task`)

管理已提交的任务。

## 列出任务

```bash
# 列出所有任务
uniq task list

# 按状态筛选
uniq task list --status success
uniq task list --status failed

# 按平台筛选
uniq task list --platform originq

# 限制显示数量
uniq task list --limit 10
```

表格输出示例：

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Tasks                              ┃
┡━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━┩
│ Task ID    │ Platform │ Status │ Shots │ Submit Time    │
├────────────┼──────────┼────────┼───────┼────────────────┤
│ TASK001    │ originq  │ success│ 1000  │ 2026-04-18 10: │
│ TASK002    │ originq  │ running│ 2000  │ 2026-04-18 11: │
└────────────┴──────────┴────────┴───────┴────────────────┘
```

## 查看任务详情

```bash
# 显示任务详情
uniq task show TASK_ID

# JSON 格式输出
uniq task show TASK_ID --format json
```

## 清理任务缓存

```bash
# 清理已完成的任务
uniq task clear --status completed

# 清理所有缓存（需确认）
uniq task clear

# 强制清理（无需确认）
uniq task clear --force
```

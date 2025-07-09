# GitHub 使用指南

## 日常更新

1. **检查状态**:

   ```bash
   git status
   ```

   - 红色：未暂存的更改
   - 绿色：已暂存等待提交的更改

2. **添加更改**:

   ```bash
   git add .
   ```

3. **提交更改**:

   ```bash
   git commit -m "更改说明"
   ```

4. **推送**:

   ```bash
   git push
   ```

## 从 GitHub 更新并处理合并

1. **获取远程更新**:

   ```bash
   git fetch origin
   ```

2. **检查是否有更新**:

   ```bash
   git status
   ```

3. **更新操作**:

   如果没有本地修改：

   ```bash
   git pull origin main
   ```

   如果有本地修改：

   ```bash
   # 先保存本地修改
   git add .
   git commit -m "保存本地更改"
   
   # 然后拉取更新
   git pull origin main
   ```

4. **处理合并冲突**:

   如果看到这样的标记：

   ```text
   <<<<<<< HEAD
   你的修改
   =======
   远程的修改
   >>>>>>> branch
   ```

   处理步骤：
   1. 编辑冲突文件
   2. 选择要保留的内容
   3. 删除冲突标记
   4. 保存并提交：

      ```bash
      git add .
      git commit -m "解决冲突"
      ```

## 上传到现有 GitHub 仓库

1. **链接远程仓库**:

   ```bash
   # 查看当前远程仓库
   git remote -v
   
   # 如果没有远程仓库，添加它（使用你的仓库 URL）
   git remote add origin https://github.com/你的用户名/仓库名.git
   
   # 或者如果需要更新现有的远程仓库 URL
   git remote set-url origin https://github.com/你的用户名/仓库名.git
   ```

2. **获取远程更新**:

   ```bash
   # 获取远程仓库的内容
   git fetch origin
   
   # 如果是首次上传，设置本地 main 分支跟踪远程分支
   git branch --set-upstream-to=origin/main main
   ```

3. **合并远程更改（如果需要）**:

   ```bash
   # 拉取并合并远程更改
   git pull origin main
   ```

4. **上传更改**:

   ```bash
   # 添加所有文件
   git add .
   
   # 提交更改
   git commit -m "初始上传" 
   
   # 推送到远程仓库
   git push -u origin main
   ```

## 建议的工作流程

1. **开始工作前更新**:

   ```bash
   git pull origin main
   ```

2. **完成后上传**:

   ```bash
   git add .
   git commit -m "更改说明"
   git push origin main
   ```

## 故障排除

1. **推送认证失败**:

   ```bash
   git remote set-url origin https://YOUR_PAT@github.com/USERNAME/REPOSITORY.git
   ```

2. **推送被拒绝**:

   ```bash
   git pull origin main
   git push origin main
   ```

3. **检查远程地址**:

   ```bash
   git remote -v
   ```

## 快速更新命令

完整更新流程：

```bash
git pull origin main && git add . && git commit -m "更新" && git push origin main
```

## 撤销操作

1. **撤销未提交的修改**:

   ```bash
   # 特定文件
   git checkout -- 文件名
   
   # 所有文件
   git checkout -- .
   ```

2. **撤销最后一次提交**:

   ```bash
   # 保留修改
   git reset --soft HEAD^
   
   # 完全撤销
   git reset --hard HEAD^
   ```

## 常见问题解决

1. **如果推送被拒绝**:

   ```bash
   # 强制推送（谨慎使用）
   git push -f origin main
   ```

2. **如果需要重新认证**:

   ```bash
   # 使用个人访问令牌（PAT）设置
   git remote set-url origin https://你的PAT@github.com/你的用户名/仓库名.git
   ```

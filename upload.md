# GitHub Upload Instructions

## Regular Updates

1. **Check Status**:

   ```bash
   git status
   ```

2. **Add New/Changed Files**:

   ```bash
   git add .
   ```

3. **Commit**:

   ```bash
   git commit -m "Description of changes"
   ```

4. **Push**:

   ```bash
   git push
   ```

## Troubleshooting

1. If push fails with authentication error:
   ```bash
   git remote set-url origin https://YOUR_PAT@github.com/USERNAME/REPOSITORY.git
   ```

2. If push is rejected:
   ```bash
   git pull origin main
   git push origin main
   ```

3. To check remote URL:
   ```bash
   git remote -v
   ```

## Quick Single-Line Upload
For quick updates, you can use this all-in-one command:
```bash
git add . && git commit -m "Update" && git push
```

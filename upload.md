# GitHub Upload Instructions

## this is not first time

## One-Time Setup

1. **Configure Git** (if not done before):

   ```bash
   git config --global user.email "supercalifragilistichsu@gmail..com"
   git config --global user.name "kenkenken0916"
   ```

2. **GitHub Authentication**:

   - Create a Personal Access Token (PAT):
     1. Go to GitHub.com → Settings → Developer Settings → Personal Access Tokens
     2. Generate a new token with 'repo' permissions
     3. Save the token somewhere safe

## Upload Steps

1. **Initialize Repository** (first time only):

   ```bash
   git init
   ```

2. **Add Files**:

   ```bash
   git add .
   ```

3. **Commit Changes**:

   ```bash
   git commit -m "Your commit message"
   ```

4. **Link to GitHub** (first time only):

   ```bash
   git remote add origin https://github.com/USERNAME/REPOSITORY.git
   git branch -M main
   ```

5. **Push to GitHub**:

   ```bash
   git push -u origin main
   ```

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

# cylqhsvideo.github.io

静态站点的云端部署配置，目标地址：<https://cylqhsvideo.github.io/>。

## 部署环境

| 项目 | 配置 |
| --- | --- |
| 托管 | GitHub Pages |
| CI 运行环境 | GitHub Actions / Ubuntu 24.04 |
| 打包工具 | 运行环境自带的 Python 3，仅使用标准库 |
| 入口文件 | 仓库根目录 `index.html` |
| 发布目录 | `_site/` |
| 自动发布 | 推送到 `main` |
| PR 检查 | 打包并上传产物，部署任务跳过 |
| 手动发布 | Actions → Deploy static site to GitHub Pages → Run workflow，选择 `main` |

当前项目是纯静态 HTML 和 MP4 文件，不需要安装 Node.js、npm 依赖、数据库或配置访问密钥。打包脚本保留网页和视频的相对路径，排除 Git 元数据、工作流、脚本和本说明，并生成 `.nojekyll`。

## 首次启用

1. 将本次配置合入仓库的 `main` 分支。如果使用配置压缩包，将包内全部文件覆盖到现有仓库根目录，保留 `.github` 和 `scripts` 的目录结构；压缩包仅含部署配置，不包含现有首页和视频。
2. 打开仓库 **Settings → Pages → Build and deployment**，将 **Source** 设为 **GitHub Actions**。此步骤需要仓库管理员或维护者权限。
3. 在 **Actions** 中打开 **Deploy static site to GitHub Pages**。如果刚才的推送任务因 Pages 尚未启用而失败，重新运行失败任务，或选择 **Run workflow → main**。
4. `Build static site` 与 `Deploy to GitHub Pages` 都成功后，打开 <https://cylqhsvideo.github.io/>。

建议在 **Settings → Environments → github-pages** 中将可部署分支限制为 `main`。工作流本身也限制了只有 `main` 的推送或手动运行才能部署。

GitHub 官方说明：[选择 Actions 作为发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)、[Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。

## 本地验证

在完整仓库根目录运行以下命令（Windows 如无 `python3` 命令，可用 `python`）：

```sh
python3 scripts/build_site.py
python3 -m http.server 8080 --directory _site
```

打开 <http://localhost:8080/>。视频可通过 `http://localhost:8080/share_5c3feeab2eb2be501ee5a534c3712550.mp4` 访问。打包命令会重建本仓库的 `_site` 目录；生成目录已加入 `.gitignore`。

## 常见情况

- **Pages 配置报错**：确认 Settings → Pages 的 Source 为 GitHub Actions，并确认 Actions 未被禁用；组织如限制 Actions，需允许本工作流使用的官方 `actions/*` 动作。
- **部署分支被环境规则拒绝**：检查 `github-pages` 环境是否允许 `main` 部署；如环境要求审核，完成该次部署审核。
- **访问 404**：先确认部署任务成功，再检查首页位于仓库根目录且文件名为小写 `index.html`。
- **首页只有原来的两字占位文本**：当前仓库的 `index.html` 就是占位内容。此配置保留网页内容，视频文件仍通过原路径访问；需要展示视频时再编辑首页。
- **回滚**：在 `main` 上还原有问题的提交，新的推送会重新发布还原后的内容。

真实上线是否成功，以 GitHub Actions 的部署结果及发布地址的访问结果为准。

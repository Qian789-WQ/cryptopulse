import sys
import os
from pathlib import Path

# 确保项目根目录在Python路径中
root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))

# 导入Flask应用
from cryptopulse.api.app import app as application

# 确保templates和static路径正确
from cryptopulse.api import app as api_app
api_app.template_folder = str(root / "cryptopulse" / "api" / "templates")
api_app.static_folder = str(root / "cryptopulse" / "api" / "static")

app = application

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask
import config
from exts import db, mail
from flask_migrate import Migrate
import models


app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

# 加载数据库到app
db.init_app(app)
mail.init_app(app)

# 可以通过migrate进行环境初始化以及自动生成迁移脚本并且映射到数据中
migrate = Migrate(app, db)
# flask db init：只需要执行一次
# flask db migrate：将orm模型生成迁移脚本
# flask db upgrade：将迁移脚本映射到数据库中


@app.route("/test")
def hello():
    return "hello easy record"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# إنشاء object للـ database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # تحميل الإعدادات من config.py
    app.config.from_object('app.config.Config')

    # ربط الـ app بالـ database
    db.init_app(app)

    # استدعاء الـ routes داخل context
    with app.app_context():
        from . import routes  # استيراد البلوبرينتات
        db.create_all()       # إنشاء الجداول لو مش موجودة

        # تسجيل البلوبرينت
        app.register_blueprint(routes.main)

    return app

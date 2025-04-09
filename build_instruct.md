### 一键生成 Django 项目和后端框架（Markdown 文档）

以下步骤将指导你如何一键生成 Django 项目与三个表格（Hotels、Reservation、Guest）的 CRUD 接口：

---

## ✅ 环境准备

### 1. 创建虚拟环境并安装依赖：
```bash
python -m venv venv
source venv/bin/activate  # Windows 用 venv\Scripts\activate
pip install django djangorestframework
```

### 2. 创建 Django 项目：
```bash
django-admin startproject hotel_project .
```

### 3. 创建应用：
```bash
python manage.py startapp hotel_app
```

---

## ✅ 项目配置

### 4. 编辑 `hotel_project/settings.py`：
确保在 `INSTALLED_APPS` 中添加：
```python
'rest_framework',
'hotel_app',
```

### 5. 添加模型代码：
在 `hotel_app/models.py` 中添加 Hotels、Reservation、Guest 三个模型（见上方代码段）。

### 6. 创建序列化器：
在 `hotel_app/serializers.py` 中添加对应序列化类（见上方代码段）。

### 7. 添加视图：
在 `hotel_app/views.py` 中添加 `ModelViewSet`（见上方代码段）。

### 8. 添加应用内路由：
在 `hotel_app/urls.py` 中注册路由（见上方代码段）。

### 9. 主路由配置：
编辑 `hotel_project/urls.py`，添加：
```python
path('api/', include('hotel_app.urls')),
```

---

## ✅ 数据库与启动

### 10. 创建数据库迁移：
```bash
python manage.py makemigrations
python manage.py migrate
```

### 11. 启动开发服务器：
```bash
python manage.py runserver
```

---

## ✅ 接口访问
你现在可以访问以下接口测试 CRUD 功能：
- `http://127.0.0.1:8000/api/hotels/`
- `http://127.0.0.1:8000/api/reservations/`
- `http://127.0.0.1:8000/api/guests/`

---

如需进一步自动化（如脚本或 Makefile），可告知我继续帮你扩展。

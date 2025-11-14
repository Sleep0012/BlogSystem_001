from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from models import db, User, Post, Comment, init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db.init_app(app)

@app.route('/')
def index():
    """首页 - 显示所有文章"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    """文章详情页"""
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    """创建新文章"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title or not content:
            flash('标题和内容不能为空！', 'error')
            return redirect(url_for('create'))
        
        # 创建新文章（暂时使用用户ID 1，实际项目中应该使用当前登录用户）
        post = Post(title=title, content=content, user_id=1)
        db.session.add(post)
        db.session.commit()
        
        flash('文章发布成功！', 'success')
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/about')
def about():
    """关于页面"""
    return render_template('about.html')

# 错误处理
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        # 创建数据库表
        db.create_all()
        # 初始化示例数据
        init_db()
    
    print("=" * 50)
    print("BlogSystem 启动成功！")
    print("访问地址: http://localhost:5000")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

# 评论系统功能 - 由feature/comment-system分支添加
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

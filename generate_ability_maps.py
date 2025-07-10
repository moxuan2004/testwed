import os

# 学员数据
students_data = [
    {'name': '蔡苏源', 'scores': [95, 80, 95, 99], 'total': 369},
    {'name': '钱诗雯', 'scores': [96, 88, 97, 95], 'total': 376},
    {'name': '董壮', 'scores': [94, 89, 96, 97], 'total': 376},
    {'name': '耿豪', 'scores': [94, 94, 98, 98], 'total': 384},
    {'name': '曹梦颖', 'scores': [93, 90, 98, 97], 'total': 378},
    {'name': '陈国丹', 'scores': [95, 92, 97, 96], 'total': 380},
    {'name': '陈娜', 'scores': [92, 89, 98, 97], 'total': 376},
    {'name': '韩钟贵', 'scores': [96, 89, 97, 96], 'total': 378},
    {'name': '程思佳', 'scores': [95, 87, 95, 98], 'total': 375},
    {'name': '胡名旺', 'scores': [95, 93, 98, 97], 'total': 383},
    {'name': '程雨瑶', 'scores': [94, 90, 96, 98], 'total': 378},
    {'name': '李捷', 'scores': [93, 92, 98, 96], 'total': 379},
    {'name': '丁梦语', 'scores': [92, 91, 96, 99], 'total': 378},
    {'name': '付青青', 'scores': [95, 90, 96, 98], 'total': 379},
    {'name': '李显阳', 'scores': [96, 91, 98, 97], 'total': 382},
    {'name': '陆俊羽', 'scores': [94, 88, 98, 96], 'total': 376},
    {'name': '李小凡', 'scores': [93, 87, 98, 97], 'total': 375},
    {'name': '年浩', 'scores': [95, 84, 96, 95], 'total': 370},
    {'name': '李卓璇', 'scores': [96, 86, 97, 98], 'total': 377},
    {'name': '蒲发清', 'scores': [97, 90, 96, 97], 'total': 380},
    {'name': '刘欣悦', 'scores': [94, 85, 98, 96], 'total': 373},
    {'name': '刘阳华', 'scores': [95, 82, 97, 97], 'total': 371},
    {'name': '沈长青', 'scores': [93, 89, 99, 95], 'total': 376},
    {'name': '王树宇', 'scores': [93, 90, 95, 97], 'total': 375},
    {'name': '吴良军', 'scores': [94, 93, 95, 98], 'total': 380},
    {'name': '吕科慧', 'scores': [94, 93, 96, 96], 'total': 379},
    {'name': '徐华剑', 'scores': [96, 92, 98, 95], 'total': 381},
    {'name': '潘馨', 'scores': [96, 95, 100, 98], 'total': 389}
]

# 生成能力分析函数
def generate_analysis(student):
    scores = student['scores']
    name = student['name']
    
    # 找出最高分和最低分的任务
    max_score = max(scores)
    min_score = min(scores)
    max_tasks = [i for i, score in enumerate(scores) if score == max_score]
    min_tasks = [i for i, score in enumerate(scores) if score == min_score]
    
    task_names = [
        '外物侵限下列车故障救援应急处置',
        '列车区间火灾下站线联动应急处置', 
        '多信号设备故障综合应急处置',
        '多设备故障时乘客突发疾病应急处置'
    ]
    
    # 生成优势分析
    strengths = []
    if max_score >= 95:
        max_task_names = [f'任务{i+1}' for i in max_tasks]
        strengths.append(f'<strong>{",".join(max_task_names)}表现突出：</strong>得分{max_score}分，展现出优秀的应急处理能力。')
    
    high_scores = [i for i, score in enumerate(scores) if score >= 95 and score != max_score]
    if high_scores:
        high_task_names = [f'任务{i+1}' for i in high_scores]
        strengths.append(f'<strong>{",".join(high_task_names)}稳定发挥：</strong>均获得高分，显示出扎实的基础技能。')
    
    if max_score >= 98:
        strengths.append('<strong>应急反应能力强：</strong>在复杂突发情况下能够保持冷静，做出正确判断。')
    
    # 生成劣势分析
    weaknesses = []
    if min_score < 90:
        min_task_names = [f'任务{i+1}' for i in min_tasks]
        weaknesses.append(f'<strong>{",".join(min_task_names)}需要加强：</strong>{task_names[min_tasks[0]]}得分{min_score}分，需要重点提升。')
    
    low_scores = [i for i, score in enumerate(scores) if score < 92 and score != min_score]
    if low_scores:
        weaknesses.append('<strong>基础技能需巩固：</strong>在某些基础操作方面还有提升空间。')
    
    if max_score - min_score > 15:
        weaknesses.append('<strong>能力均衡性：</strong>各项任务之间的能力差异较大，需要均衡发展。')
    
    return strengths, weaknesses

# HTML模板
html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - 个人能力图谱</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            text-align: center;
            margin-bottom: 30px;
            color: white;
        }}

        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}

        .back-btn {{
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: 2px solid white;
            padding: 10px 20px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
        }}

        .back-btn:hover {{
            background: white;
            color: #667eea;
            transform: translateY(-2px);
        }}

        .chart-container {{
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}

        .student-info {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .student-name {{
            font-size: 2.5em;
            color: #2c3e50;
            margin-bottom: 10px;
            font-weight: bold;
        }}

        .student-total {{
            font-size: 1.5em;
            color: #e74c3c;
            font-weight: bold;
            margin-bottom: 20px;
        }}

        .ability-overview {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}

        .ability-card {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}

        .ability-card:hover {{
            transform: translateY(-5px);
        }}

        .ability-score {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }}

        .ability-label {{
            font-size: 1em;
            opacity: 0.9;
            line-height: 1.4;
        }}

        .radar-section {{
            margin-bottom: 40px;
        }}

        .radar-chart {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 40px 0;
        }}

        .radar-canvas {{
            border: 2px solid #ecf0f1;
            border-radius: 15px;
            background: #fafafa;
        }}

        .analysis-section {{
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
        }}

        .analysis-title {{
            font-size: 1.8em;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
            font-weight: bold;
        }}

        .strength-weakness {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 20px;
        }}

        .strength, .weakness {{
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }}

        .strength {{
            border-left: 5px solid #2ecc71;
        }}

        .weakness {{
            border-left: 5px solid #e74c3c;
        }}

        .section-title {{
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 15px;
            color: #2c3e50;
        }}

        .strength .section-title {{
            color: #2ecc71;
        }}

        .weakness .section-title {{
            color: #e74c3c;
        }}

        .recommendation {{
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin-top: 20px;
        }}

        .recommendation-title {{
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 15px;
        }}

        .recommendation-list {{
            list-style: none;
            padding: 0;
        }}

        .recommendation-list li {{
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
        }}

        .recommendation-list li:before {{
            content: "💡";
            position: absolute;
            left: 0;
        }}

        @media (max-width: 768px) {{
            .strength-weakness {{
                grid-template-columns: 1fr;
            }}
            
            .ability-overview {{
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            }}
        }}
    </style>
</head>
<body>
    <a href="task1.html" class="back-btn">← 返回成绩表</a>
    
    <div class="container">
        <div class="header">
            <h1>🎯 个人能力图谱</h1>
            <p>四项任务综合能力分析</p>
        </div>

        <div class="chart-container">
            <div class="student-info">
                <div class="student-name">{name}</div>
                <div class="student-total">综合分：{total}分</div>
            </div>

            <div class="ability-overview">
                <div class="ability-card">
                    <div class="ability-score">{score1}</div>
                    <div class="ability-label">任务一<br>外物侵限下列车故障救援应急处置</div>
                </div>
                <div class="ability-card">
                    <div class="ability-score">{score2}</div>
                    <div class="ability-label">任务二<br>列车区间火灾下站线联动应急处置</div>
                </div>
                <div class="ability-card">
                    <div class="ability-score">{score3}</div>
                    <div class="ability-label">任务三<br>多信号设备故障综合应急处置</div>
                </div>
                <div class="ability-card">
                    <div class="ability-score">{score4}</div>
                    <div class="ability-label">任务四<br>多设备故障时乘客突发疾病应急处置</div>
                </div>
            </div>

            <div class="radar-section">
                <div class="radar-chart">
                    <canvas id="radarCanvas" width="500" height="500" class="radar-canvas"></canvas>
                </div>
            </div>

            <div class="analysis-section">
                <div class="analysis-title">📊 能力分析报告</div>
                
                <div class="strength-weakness">
                    <div class="strength">
                        <div class="section-title">💪 优势能力</div>
                        {strengths}
                    </div>
                    
                    <div class="weakness">
                        <div class="section-title">🎯 提升空间</div>
                        {weaknesses}
                    </div>
                </div>

                <div class="recommendation">
                    <div class="recommendation-title">🚀 能力提升建议</div>
                    <ul class="recommendation-list">
                        {recommendations}
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <script>
        // 绘制雷达图
        function drawRadarChart() {{
            const canvas = document.getElementById('radarCanvas');
            const ctx = canvas.getContext('2d');
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2;
            const radius = 180;
            const maxScore = 100;
            
            // 学员数据
            const scores = [{score1}, {score2}, {score3}, {score4}];
            const labels = ['任务一', '任务二', '任务三', '任务四'];
            const colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12'];
            
            // 清空画布
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // 绘制背景网格
            ctx.strokeStyle = '#ddd';
            ctx.lineWidth = 1;
            
            // 绘制同心圆
            for (let i = 1; i <= 5; i++) {{
                ctx.beginPath();
                ctx.arc(centerX, centerY, (radius * i) / 5, 0, 2 * Math.PI);
                ctx.stroke();
            }}
            
            // 绘制轴线和标签
            ctx.strokeStyle = '#bbb';
            ctx.fillStyle = '#2c3e50';
            ctx.font = 'bold 14px Microsoft YaHei';
            ctx.textAlign = 'center';
            
            for (let i = 0; i < 4; i++) {{
                const angle = (i * Math.PI) / 2 - Math.PI / 2;
                const x1 = centerX + Math.cos(angle) * radius;
                const y1 = centerY + Math.sin(angle) * radius;
                
                // 绘制轴线
                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.lineTo(x1, y1);
                ctx.stroke();
                
                // 绘制标签
                const labelX = centerX + Math.cos(angle) * (radius + 30);
                const labelY = centerY + Math.sin(angle) * (radius + 30);
                ctx.fillText(labels[i], labelX, labelY + 5);
                
                // 绘制分数标签
                ctx.fillStyle = colors[i];
                ctx.font = 'bold 16px Microsoft YaHei';
                const scoreX = centerX + Math.cos(angle) * (radius + 60);
                const scoreY = centerY + Math.sin(angle) * (radius + 60);
                ctx.fillText(scores[i], scoreX, scoreY + 5);
                ctx.fillStyle = '#2c3e50';
                ctx.font = 'bold 14px Microsoft YaHei';
            }}
            
            // 绘制数据区域
            ctx.fillStyle = 'rgba(52, 152, 219, 0.2)';
            ctx.strokeStyle = '#3498db';
            ctx.lineWidth = 3;
            
            ctx.beginPath();
            for (let i = 0; i < 4; i++) {{
                const angle = (i * Math.PI) / 2 - Math.PI / 2;
                const score = scores[i];
                const distance = (score / maxScore) * radius;
                const x = centerX + Math.cos(angle) * distance;
                const y = centerY + Math.sin(angle) * distance;
                
                if (i === 0) {{
                    ctx.moveTo(x, y);
                }} else {{
                    ctx.lineTo(x, y);
                }}
            }}
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // 绘制数据点
            for (let i = 0; i < 4; i++) {{
                const angle = (i * Math.PI) / 2 - Math.PI / 2;
                const score = scores[i];
                const distance = (score / maxScore) * radius;
                const x = centerX + Math.cos(angle) * distance;
                const y = centerY + Math.sin(angle) * distance;
                
                ctx.fillStyle = colors[i];
                ctx.beginPath();
                ctx.arc(x, y, 8, 0, 2 * Math.PI);
                ctx.fill();
                
                // 添加白色边框
                ctx.strokeStyle = 'white';
                ctx.lineWidth = 2;
                ctx.stroke();
            }}
            
            // 绘制分数刻度
            ctx.fillStyle = '#7f8c8d';
            ctx.font = '12px Microsoft YaHei';
            ctx.textAlign = 'center';
            
            for (let i = 1; i <= 5; i++) {{
                const score = (i * 20);
                const y = centerY - (radius * i) / 5;
                ctx.fillText(score, centerX - 15, y + 4);
            }}
        }}

        // 页面加载时绘制雷达图
        document.addEventListener('DOMContentLoaded', function() {{
            drawRadarChart();
        }});
    </script>
</body>
</html>'''

# 为每个学员生成能力图谱文件
for student in students_data:
    name = student['name']
    scores = student['scores']
    total = student['total']
    
    # 生成分析内容
    strengths, weaknesses = generate_analysis(student)
    
    # 生成建议
    recommendations = [
        '加强薄弱环节的理论学习和实操训练',
        '参与更多应急演练，提升实战经验',
        '学习优秀案例，总结应急处置的最佳实践',
        '保持优势能力，发挥专业特长',
        '注重各项技能的均衡发展'
    ]
    
    # 格式化内容
    strengths_html = ''.join([f'<p>{s}</p>' for s in strengths]) if strengths else '<p>继续保持当前水平，各项能力均衡发展。</p>'
    weaknesses_html = ''.join([f'<p>{w}</p>' for w in weaknesses]) if weaknesses else '<p>各项能力表现均衡，继续保持。</p>'
    recommendations_html = ''.join([f'<li>{r}</li>' for r in recommendations])
    
    # 生成HTML内容
    html_content = html_template.format(
        name=name,
        total=total,
        score1=scores[0],
        score2=scores[1], 
        score3=scores[2],
        score4=scores[3],
        strengths=strengths_html,
        weaknesses=weaknesses_html,
        recommendations=recommendations_html
    )
    
    # 写入文件
    filename = f'ability-map-{name}.html'
    filepath = os.path.join(r'c:\Users\Admin\Desktop\总体文件夹\专业二', filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'已生成 {name} 的能力图谱文件: {filename}')

print('\n所有学员的能力图谱文件生成完成！')
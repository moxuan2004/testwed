import json
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

# 计算每个学生的能力维度得分
processed_data = []
for student in students_data:
    tech_score = (student['scores'][0] + student['scores'][2]) / 2
    coord_score = (student['scores'][1] + student['scores'][3]) / 2
    processed_data.append({
        'name': student['name'],
        'value': [tech_score, coord_score, student['total']]
    })

# HTML 模板
html_template = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>就业方向能力象限分析</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.3.3/dist/echarts.min.js"></script>
    <style>
        body {{ font-family: 'Microsoft YaHei', sans-serif; background-color: #f4f7f9; color: #333; margin: 0; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; background-color: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
        h1, h2 {{ text-align: center; color: #2c3e50; }}
        #scatter-chart {{ width: 100%; height: 700px; margin: 20px 0; }}
        .info-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px; }}
        .quadrant-info {{ background-color: #ecf0f1; padding: 20px; border-radius: 8px; }}
        .quadrant-info h3 {{ color: #2980b9; margin-top: 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>就业方向能力象限分析</h1>
        <div id="scatter-chart"></div>
        <h2>能力象限解读</h2>
        <div class="info-grid">
            <div class="quadrant-info">
                <h3>第一象限 (技术专家型)</h3>
                <p><strong>特点:</strong> 技术应用能力和应急协调能力双高。<br><strong>就业方向:</strong> 高级行车调度员、车站站长、应急指挥、技术培训师。</p>
            </div>
            <div class="quadrant-info">
                <h3>第二象限 (技术专精型)</h3>
                <p><strong>特点:</strong> 技术应用能力突出，应急协调能力有待提升。<br><strong>就业方向:</strong> 信号系统工程师、设备维护专家、技术支持。</p>
            </div>
            <div class="quadrant-info">
                <h3>第三象限 (潜力发展型)</h3>
                <p><strong>特点:</strong> 两项能力均有较大提升空间。<br><strong>就业方向:</strong> 初级岗位，需加强综合实训，全面发展。</p>
            </div>
            <div class="quadrant-info">
                <h3>第四象限 (协调管理型)</h3>
                <p><strong>特点:</strong> 应急协调能力突出，技术应用能力有待提升。<br><strong>就业方向:</strong> 乘客服务主管、安全监督员、运营协调。</p>
            </div>
        </div>
    </div>

    <script>
        var chart = echarts.init(document.getElementById('scatter-chart'));
        var data = {processed_data_json};

        var option = {{
            xAxis: {{ name: '技术应用能力', min: 85, max: 100, splitLine: {{ show: true }} }},
            yAxis: {{ name: '应急协调能力', min: 80, max: 100, splitLine: {{ show: true }} }},
            tooltip: {{
                formatter: function (params) {{
                    return params.data.name + '<br/>' +
                           '技术应用: ' + params.data.value[0].toFixed(2) + '<br/>' +
                           '应急协调: ' + params.data.value[1].toFixed(2) + '<br/>' +
                           '总分: ' + params.data.value[2];
                }}
            }},
            series: [{{
                name: '学员',
                type: 'scatter',
                symbolSize: function (data) {{
                    return (data[2] - 360) * 1.5; // 根据总分调整点的大小
                }},
                data: data,
                label: {{ show: true, formatter: '{{b}}' }},
                markArea: {{
                    silent: true,
                    itemStyle: {{ color: 'rgba(200, 220, 255, 0.2)' }},
                    data: [
                        [ {{ name: '技术专家型', xAxis: '92.5', yAxis: '90' }}, {{ xAxis: '100', yAxis: '100' }} ],
                        [ {{ name: '技术专精型', xAxis: '92.5', yAxis: '80' }}, {{ xAxis: '100', yAxis: '90' }} ],
                        [ {{ name: '潜力发展型', xAxis: '85', yAxis: '80' }}, {{ xAxis: '92.5', yAxis: '90' }} ],
                        [ {{ name: '协调管理型', xAxis: '85', yAxis: '90' }}, {{ xAxis: '92.5', yAxis: '100' }} ]
                    ]
                }}
            }}]
        }};

        chart.setOption(option);
    </script>
</body>
</html>
'''

# 生成最终的HTML内容
final_html = html_template.format(processed_data_json=json.dumps(processed_data))

# 写入文件
filename = 'employment_scatter_plot.html'
filepath = os.path.join(r'c:\Users\Admin\Desktop\总体文件夹\专业二', filename)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f'已生成新的就业方向分析文件: {filename}')
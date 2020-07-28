import importlib
import json
import os
import sys
import pandas as pd
import time
from pyecharts.charts import Line,Bar,Pie
from pyecharts import options as opts

import os


def all_path(dirname):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)

    return result


def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.png':
                L.append(os.path.join(root, file))
    return L


importlib.reload(sys)

f = open('test_data.json', encoding='utf-8')
res = f.read()

data = json.loads(res)
list1=file_name("C:/Users/lenovo/Desktop/录屏&截图/面向用例")
profile=all_path("C:/Users/lenovo/PycharmProjects/codeReview")
S=[]
for i in range(len(profile)):
    str1=profile[i].split('/')
    str2=str1[4].split('\\')
    if(len(str2)>2):
        if(str2[1][0].isnumeric()):
            S.append(str2[1])
M=[]
RES=[]
count1=0
for i in range(len(S)-1):
    if(S[i]==S[i+1]):
        S[i]=str(0)
for i in range(len(S)):
    M=S[i].split('_')
    if(len(M))==3:
        RES.append(M)
name=[]
for i in range(len(list1)):
    list2=list1[i].split('/')
    list3=list2[5].split('\\')
    list4=list3[1].split('.')
    list5=list4[0].split('_')
    name.append(list5)
res1=['60602', '60606', '60611', '60621', '60625', '60625', '60644', '60644', '60649', '60649', '60651', '60658', '60658', '60667', '60667', '60688', '60688', '60696', '60703', '60703', '60705', '60705', '60716', '60716', '60731', '60731', '60738', '60738', '60758', '60791', '60791', '60793', '60828', '60833', '60839', '60839', '61048', '61519', '8246', '8317', '8318']
res2=['2912', '2151', '2717', '2175', '2343', '2717', '2343', '2717', '2343', '2717', '2912', '2175', '2912', '2343', '2717', '2175', '2912', '2151', '2175', '2912', '2672', '2717', '2175', '2912', '2343', '2717', '2175', '2912', '2717', '2343', '2717', '2717', '2912', '2151', '2343', '2717', '2717', '2912', '2717', '2717', '2717']
ifs=[1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 4, 1, 2, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ps=[100, 100 , 100, 100, 100, 100, 100, 100, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 50.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
for i in range(len(res1)):
    list5=[]
    list5.append(res1[i])
    list5.append(res2[i])
    name.append(list5)
result=[]
for i in range(len(res1)):
    result.append(res1[i]+"_"+res2[i])
for i in range(len(ps)):
    ps[i]=ps[i]/100
uploads_nums=[]
case_nums=[]
for i in range(len(name)):
    cases=data[name[i][0]]["cases"]
    m=0
    for case in cases:
        if case["case_id"]==name[i][1]:
            scores=[]
            nums=[]
            times=[]
            time_res=[]
            records=case["upload_records"]
            if i<16:
                uploads_nums.append(len(records))
            for record in records:
                scores.append(record["score"])
                times.append(record["upload_time"])

            for n in range(len(times)):
                timeStamp = int(str(times[n])[:-3])
                timeArray = time.localtime(timeStamp)
                otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
                time_res.append(otherStyleTime)
            for j in range(len(scores)):
                ost=(str(time_res[j])[6:].replace('--','-'))
                temp_list=ost.split(' ')
                t_l=temp_list[0].split('-')
                if(t_l[0][0]=='0'):
                    t_l[0]=t_l[0].replace('0','')
                nums.append('第'+str(j+1)+'次:'+t_l[0]+"-"+t_l[1]+" "+temp_list[1][:-3])
            print(nums)
            line = (
                Line()
                    .add_xaxis(xaxis_data=nums)
                    .add_yaxis(
                    series_name="分数",
                    y_axis= scores,
                    label_opts=opts.LabelOpts(is_show=True),
                )
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title="提交次数与分数的折线图"),
                    tooltip_opts=opts.TooltipOpts(
                        is_show=True, trigger="axis", axis_pointer_type="cross"
                    ),
                    xaxis_opts=opts.AxisOpts(
                        name="提交次数/时间",
                        axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
                    ),
                    yaxis_opts=opts.AxisOpts(
                        name="提交分数",
                        type_="value",
                        axislabel_opts=opts.LabelOpts(formatter="{value}"),
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    )
                ))
            line.render(name[i][0]+'_'+name[i][1]+'.html')
            m=m+1
for i in range(len(S)-1):
    if(S[i]==S[i+1]):
        S[i]=str(0)
named=[]
for i in range(len(name)):
    for j in range(len(RES)):
        if (RES[j][0]==name[i][0])and(RES[j][1]==name[i][1]):
            named.append(RES[j][0]+'_'+RES[j][1])
            file = open(RES[j][0]+'_'+RES[j][1]+'_'+RES[j][2] + '/.mooctest' + '/testCases.json', encoding='utf-8')
            fi = file.read()
            data_testCase = json.loads(fi)
            case_nums.append(len(data_testCase))
bar1=(Bar()
       .add_xaxis(named)
       .add_yaxis('面向用例样本的提交次数',uploads_nums)
       .add_yaxis('样本所属case的用例数',case_nums)
       .set_global_opts(title_opts=opts.TitleOpts(title="提交次数与用例数"))
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
       .reversal_axis()
)
bar1.render("bar_case.html")
bar=(Bar()
       .add_xaxis(result)
       .add_yaxis('if_else数',ifs)
       .add_yaxis('print占代码比率', ps)
       .set_global_opts(title_opts=opts.TitleOpts(title="面向用例样本的if_else数以及print率"))
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
       .reversal_axis()
)
bar.render("BAR.html")

inner_x_data = ["筛选疑似面向用例", "其他"]
inner_y_data = [80,691-80]
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

outer_x_data = ["面向用例（证实）", "非面向用例", "其他"]
outer_y_data = [16,80-16,691-80]
outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]

(
    Pie(init_opts=opts.InitOpts(width="800px", height="500px"))
    .add(
        series_name="总体",
        data_pair=inner_data_pair,
        radius=[0, "30%"],
        label_opts=opts.LabelOpts(position="inner"),
    )
    .add(
        series_name="是否面向用例",
        radius=["40%", "55%"],
        data_pair=outer_data_pair,
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="right", orient="vertical"),title_opts=opts.TitleOpts(title="面向用例比例"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
    .render("nested_pies.html")
)

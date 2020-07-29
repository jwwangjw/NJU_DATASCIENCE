import cmath
from pyecharts.charts import Pie,Bar
import random
from pyecharts import options as opts



named=['2912', '2151', '2717', '2175', '2343', '2672']
li=[9, 3, 15, 6, 7, 1]
str="192，200，200，200，200，200，198，199，196，199，200，199，200，200"
li2=[1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1]
for i in range(len(li2)):
    li2[i]=int(li2[i])
res1=[]
for i in range(len(li)):
    res1.append(li[i]/50)
list1=[2, 3, 2, 3, 1, 2, 2, 7, 2, 1, 2, 6, 5, 3]
list2=[]
for i in range(len(list1)):
    list2.append(200)
print(len(list1))
nums1=[]
i=0
while(len(nums1)<len(list1)):
    nums1.append(list1[i]/list2[i])
    i=i+1
while(len(nums1)<50):
    nums1.append(0)
list3=[1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1]
list4=[]
for i in range(len(list3)):
    list4.append(200)
num2=[]
j=0
while(len(num2)<len(list3)):
    num2.append(list3[j]/list4[j])
    j=j+1
while(len(num2)<50):
    num2.append(0)
res=[]
for m in range(50):
    res.append(nums1[m]*num2[m])
num3=[]
num4=[]
for n in range(len(nums1)):
    num3.append(nums1[n]*nums1[n])
    num4.append(num2[n]*num2[n])
sum1=sum(res)
sum2=sum(nums1)*sum(num2)
sum3=sum(num3)
sum4=sum(num4)
result=((50*sum1)-sum(nums1)*sum(num2))/(((50*sum3-sum(nums1)*sum(nums1))**0.5)*((50*sum4-sum(num2)*sum(num2))**0.5))
print(result)
bar1 = (Bar()
        .add_xaxis(named)
        .add_yaxis('单一用例使用面向用例同学占比', res1)
        .set_global_opts(title_opts=opts.TitleOpts(title="面向用例占比"),
                         xaxis_opts=opts.AxisOpts(name="面向用例率"),
                         yaxis_opts=opts.AxisOpts(name="Case_ID"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .reversal_axis()
        )
bar1.render("barc.html")
c = (

    Pie()

    .add("", [list(z) for z in zip(["有同学使用了面向用例的题目", "未使用面向用例的题目"], [13.5, 100-13.5])],)

    .set_global_opts(title_opts=opts.TitleOpts(title="有同学使用了面向用例"
                                                     "\n的题目占样本的比例"))

    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))

    .render("pie_base1.html")

)

"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers

from zyq import views, extract_feature, DecisionTree, utils, AMMI, GGE, AMMI_select, GGE_select, boxplot, heat
from zyq.models import rule_table, decisionTree_img
from zyq.views import BlogViewSet, SaveFileViewSet, lineChartViewSet, pieChartViewSet, rule_tableViewSet, \
    decisionTree_imgViewSet, QxViewSet
from zyq.views import regional_sampleViewSet
from zyq.views import forsetViewSet
from zyq.views import poplarViewSet
from zyq.views import treeTmpViewSet
from zyq.views import tree1ViewSet
from zyq.views import videoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

# 在django rest framework中注册api视图，api/xx
router.register('blog', BlogViewSet)
router.register('qx', QxViewSet)
router.register('regional_sample', regional_sampleViewSet)
router.register('tree1', tree1ViewSet)
router.register('poplar', poplarViewSet)
router.register('forset', forsetViewSet)
router.register('video', videoViewSet)
router.register('treeTmp', treeTmpViewSet)
router.register('SaveFile', SaveFileViewSet)

router.register('rule_table', rule_tableViewSet)
router.register('decisionTree_img', decisionTree_imgViewSet)

urlpatterns = [
    #############################写在view.py中的api######
    # test api ,http://127.0.0.1:8000/api/test/
    path('api/test/', views.test.as_view(), name="test"),
    path('api/compute_date/', views.compute_date.as_view(), name="compute_date"),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # 上传视频api,http://127.0.0.1:8000/api/evaluatefileupload/
    path('api/evaluatefileupload/', views.EvaluateFileUploadView.as_view(), name="evaluatefileupload"),
    # 查询视频api，http://127.0.0.1:8000/api/videoSearch/
    path('api/videoSearch/', views.videoSearch.as_view(), name="videoSearch"),
    path('', TemplateView.as_view(template_name='index.html')),
    # 登录api，http://127.0.0.1:8000/api/login/
    path('api/login/', views.login.as_view(), name="login"),
    # 注册api，http://127.0.0.1:8000/api/register/
    path('api/register/', views.register.as_view(), name="register"),
    # 修改用户信息api,http://127.0.0.1:8000/api/modifyUser/
    path('api/modifyUser/', views.modifyUser.as_view(), name="modifyUser"),
    # 修改用户密码api,http://127.0.0.1:8000/api/modifyPassword/
    path('api/modifyPassword/', views.modifyPassword.as_view(), name="modifyPassword"),
    # 上传excel api,http://127.0.0.1:8000/api/uploadExcel/
    path('api/uploadExcel/', views.uploadExcel.as_view(), name="uploadExcel"),
    # 特征提取api,http://127.0.0.1:8000/api/extract_feature/
    path('api/extract_feature/', views.extract_feature.as_view(), name="extract_feature"),
    # excel_to_csv api,http://127.0.0.1:8000/api/excel_to_csv/
    path('api/excel_to_csv/', views.excel_to_csv.as_view(), name="excel_to_csv"),
    # excel_to_npy api,http://127.0.0.1:8000/api/excel_to_npy/
    path('api/excel_to_npy/', views.excel_to_npy.as_view(), name="excel_to_npy"),
    # batch_deletion api,http://127.0.0.1:8000/api/batch_deletion/
    path('api/batch_deletion/', views.batch_deletion.as_view(), name="batch_deletion"),
    # batch_deletion api,http://127.0.0.1:8000/api/draw_2d_scatter/
    path('api/draw_2d_scatter/', views.draw_2d_scatter.as_view(), name="draw_2d_scatter"),
    # 上传excel 画散点图 api,http://127.0.0.1:8000/api/upload_for_scatter/
    path('api/upload_for_scatter/', views.upload_for_scatter.as_view(), name="upload_for_scatter"),

    #############################不写在view.py中的api######
    # 规则提取api,http://127.0.0.1:8000/api/extract_rule/
    path('api/extract_rule/', DecisionTree.extract_rule.as_view(), name="extract_rule"),
    # 将生成的决策树规则保存在数据库中 api ,http://127.0.0.1:8000/api/saveRule/
    path('api/saveRule/', utils.TreeToRule.saveRule.as_view(), name="saveRule"),
    # test api ,http://127.0.0.1:8000/api/draw_roc/
    path('api/draw_roc/', extract_feature.draw_roc.as_view(), name="draw_roc"),
    # GGE_1 api ,http://127.0.0.1:8000/api/GGE_1/
    # path('api/GGE_1/', GGE.get_GGE_1.as_view(), name="GGE_1"),
    # # GGE_2 api ,http://127.0.0.1:8000/api/GGE_2/
    # path('api/GGE_2/', GGE.get_GGE_2.as_view(), name="GGE_2"),

    # 上传excel 画ammi图 api,http://127.0.0.1:8000/api/upload_for_ammi/
    path('api/upload_for_ammi/', AMMI.upload_for_ammi.as_view(), name="upload_for_ammi"),
    path('api/draw_ammi/', AMMI.draw_ammi.as_view(), name="draw_ammi"),
    path('api/upload_for_variety_yield_and_stability/', GGE.upload_for_variety_yield_and_stability.as_view(),
         name="upload_for_variety_yield_and_stability"),
    path('api/draw_variety_yield_and_stability/', GGE.draw_variety_yield_and_stability.as_view(),
         name="draw_variety_yield_and_stability"),
    path('api/upload_for_which_won_where/', GGE.upload_for_which_won_where.as_view(),
         name="upload_for_which_won_where"),
    path('api/draw_which_won_where/', GGE.draw_which_won_where.as_view(),
         name="draw_which_won_where"),
    path('api/select_for_ammi/', AMMI_select.select_for_ammi.as_view(), name="select_for_ammi"),
    path('api/select_for_variety_yield_and_stability/', GGE_select.select_for_variety_yield_and_stability.as_view(), name="select_for_variety_yield_and_stability"),
    path('api/select_for_which_won_where/', GGE_select.select_for_which_won_where.as_view(), name="select_for_which_won_where"),
    path('api/select_for_scatter/', views.select_for_scatter.as_view(),
         name="select_for_scatter"),
    path('api/draw_box_plot_dq/', boxplot.draw_box_plot_dq.as_view(),
         name="draw_box_plot_dq"),
    path('api/draw_box_plot_qq/', boxplot.draw_box_plot_qq.as_view(),
         name="draw_box_plot_qq"),
    path('api/heat_dq/', heat.draw_heat_dq.as_view(),
         name="heat_dq"),
    path('api/heat_qq/', heat.draw_heat_qq.as_view(),
         name="heat_qq"),
    path('api/heat_xhy/', heat.draw_heat_xhy.as_view(),
         name="heat_xhy"),
    path('api/heat_hqy/', heat.draw_heat_hqy.as_view(),
         name="heat_hqy"),
    path('api/heat_yzy/', heat.draw_heat_yzy.as_view(),
         name="heat_yzy"),
    path('api/heat_qsy/', heat.draw_heat_qsy.as_view(),
         name="heat_qsy"),

]
# 配置访问media目录下的上传文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

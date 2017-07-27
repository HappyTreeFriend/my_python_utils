#!/usr/bin/env python
#-*-coding:utf-8-*-
#Created by happytree on 28/3/17.
#Description :

import bs4

class MyWebpage(object):

    def __init__(self, content):
        self.content = content
        self.soup = bs4.BeautifulSoup(self.content, "html.parser")

    def format_print(self):
        return self.soup.prettify()

    def find_element_id(self, id_name):
        return self.soup.find_all(id=id_name)[0]

    def find_element_tag(self, tag, tag_name):
        return tag.find_all(tag_name)

    def get_list_info(self, tag_list, attr_name, re_str):
        list_info = []
        for tag in tag_list:
            list_info.append(tag.get(attr_name).replace(re_str, "").encode("utf-8"))
        return list_info


if __name__ == "__main__":
    init_html = """<div id="app_sidebar">
                <div id="app_sidebar_white">

<!--打卡-->
<div id="task_card">
    <div id="my_hb_btn" class="floatright">
        <a style="width:72px" class="btn btnGray2 hascard mt5" title="点击查看我的打卡详情" href="###" onclick="toggleCardInfo();return false;"><span>已打卡<span></span></span></a></div>
    <ul id="coin_center">
        <li id="my_hb" style="width:146px"><span class="gray" title="沪元是沪江社区的会员虚拟积分，代表了你在沪江学习和活动的成果。">我的沪元(新)：</span><span id="mycoins" class="noline orange bold">452</span> <a class="old_hu_help" href="/account/exchange" target="_blank"><img src="/app/images/help-hy.png"></a></li>
        <li id="my_xb"><span class="gray" title="学币是沪江虚拟币，可用于兑换网校课程等">我的学币：</span><a class="orange bold noline" href="http://class.hujiang.com/xb/" target="_blank">31.4</a></li>
    </ul>
    <div class="clear">
    </div>
</div>

<!-- 勋章板块 -->
<div class="home_stau">
    <div id="myMedal">
        <div class="medal_rt">
            <a title="上一页" id="medal_prev_g" href="###"><img src="/images/spacer.gif" width="11" height="19"></a> <a title="下一页" onclick="doMedalView(2);" id="medal_next" href="###"><img src="/images/spacer.gif" width="11" height="19"></a>
        </div>
        <div class="medal_lt">

                    <a href="/u/2128764/medal/?mid=401" title="网校学苗">
                        <img src="/app/medal/images/class_mark_1_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=101" title="网校虾米">
                        <img src="/app/medal/images/class_daka_1_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=102" title="网校大虾">
                        <img src="/app/medal/images/class_daka_2_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=103" title="网校龙虾 ">
                        <img src="/app/medal/images/class_daka_3_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=201" title="词场新人">
                        <img src="/app/medal/images/class_word_1_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=202" title="振振有词">
                        <img src="/app/medal/images/class_word_2_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=203" title="大辞海">
                        <img src="/app/medal/images/class_word_3_s.gif" height="25" width="25" alt=""></a>

                    <a href="/u/2128764/medal/?mid=301" title="勤学好问">
                        <img src="/app/medal/images/class_qa_1_s.gif" height="25" width="25" alt=""></a>

        </div>
    </div>
</div>

                    <div style="position: absolute; width: 1px; height: 1px; z-index: 1; overflow: hidden;" id="hidemp3">
                    </div>

<div id="PanelTask" style="display:none;">
</div>
<div class="clear">
</div>
<div id="task_link">
    <ul>
        <!--  -->

                <li id="task_item_10831" class="newtask">
                    <a class="floatright gray noline" href="http://st.hujiang.com/topic/1711395882103/" onclick="doTaskLinkClick(0,10831,'第一届挑战视频王大赛！','2')" target="_blank">
                        +2</a> <a href="http://st.hujiang.com/topic/1711395882103/" onclick="doTaskLinkClick(0,10831,'第一届挑战视频王大赛！','2')" target="_blank" class="noline jobLink">
                            <span id="link_10831" style="">第一届挑战视频王大赛！</span></a>
                </li>

                <li id="task_item_10776" class="newtask">
                    <a class="floatright gray noline" href="http://cctalk.hujiang.com/v/14901663182414" onclick="doTaskLinkClick(0,10776,'牛人教你从零开始做网站！','1')" target="_blank">
                        +1</a> <a href="http://cctalk.hujiang.com/v/14901663182414" onclick="doTaskLinkClick(0,10776,'牛人教你从零开始做网站！','1')" target="_blank" class="noline jobLink">
                            <span id="link_10776" style="">牛人教你从零开始做网站！</span></a>
                </li>

                <li id="task_item_10810">
                    <a class="floatright gray noline" href="http://st.hujiang.com/topic/1711421291366/" onclick="doTaskLinkClick(4484,10810,'【招募】寻找CCtalk品课师','1')" target="_blank">
                        +1</a> <a href="http://st.hujiang.com/topic/1711421291366/" onclick="doTaskLinkClick(4484,10810,'【招募】寻找CCtalk品课师','1')" target="_blank" class="noline jobLink">
                            <span id="link_10810" style="text-decoration:line-through;">【招募】寻找CCtalk品课师</span></a>
                </li>

                <li id="task_item_10868" class="newtask">
                    <a class="floatright gray noline" href="http://cctalk.hujiang.com/v/14894770682945" onclick="doTaskLinkClick(0,10868,'揭秘“星巴克”的隐藏菜单','1')" target="_blank">
                        +1</a> <a href="http://cctalk.hujiang.com/v/14894770682945" onclick="doTaskLinkClick(0,10868,'揭秘“星巴克”的隐藏菜单','1')" target="_blank" class="noline jobLink">
                            <span id="link_10868" style="">揭秘“星巴克”的隐藏菜单</span></a>
                </li>

                <li id="task_item_10847" class="newtask">
                    <a class="floatright gray noline" href="http://cctalk.hujiang.com/v/14891130557276" onclick="doTaskLinkClick(0,10847,'三节课速成Word达人','1')" target="_blank">
                        +1</a> <a href="http://cctalk.hujiang.com/v/14891130557276" onclick="doTaskLinkClick(0,10847,'三节课速成Word达人','1')" target="_blank" class="noline jobLink">
                            <span id="link_10847" style="">三节课速成Word达人</span></a>
                </li>

                <li id="task_item_10833" class="newtask">
                    <a class="floatright gray noline" href="http://cctalk.hujiang.com/v/14897404432988" onclick="doTaskLinkClick(0,10833,'这一招让你拍照变高大上','1')" target="_blank">
                        +1</a> <a href="http://cctalk.hujiang.com/v/14897404432988" onclick="doTaskLinkClick(0,10833,'这一招让你拍照变高大上','1')" target="_blank" class="noline jobLink">
                            <span id="link_10833" style="">这一招让你拍照变高大上</span></a>
                </li>

                <li id="task_item_10830" class="newtask">
                    <a class="floatright gray noline" href="http://cctalk.hujiang.com/v/14902366355928" onclick="doTaskLinkClick(0,10830,'初入职场小心这5个坑','1')" target="_blank">
                        +1</a> <a href="http://cctalk.hujiang.com/v/14902366355928" onclick="doTaskLinkClick(0,10830,'初入职场小心这5个坑','1')" target="_blank" class="noline jobLink">
                            <span id="link_10830" style="">初入职场小心这5个坑</span></a>
                </li>

                <li id="task_item_10891" class="newtask">
                    <a class="floatright gray noline" href="http://cctalk.hujiang.com/m/zhuanti/100442" onclick="doTaskLinkClick(0,10891,'PPT太丑，被开除？有救！','1')" target="_blank">
                        +1</a> <a href="http://cctalk.hujiang.com/m/zhuanti/100442" onclick="doTaskLinkClick(0,10891,'PPT太丑，被开除？有救！','1')" target="_blank" class="noline jobLink">
                            <span id="link_10891" style="">PPT太丑，被开除？有救！</span></a>
                </li>

                <li id="task_item_4308" class="newtask">
                    <a class="floatright gray noline" href="http://st.hujiang.com/topic/1711421463204/" onclick="doTaskLinkClick(0,4308,'你与人生赢家间差哪？','1')" target="_blank">
                        +1</a> <a href="http://st.hujiang.com/topic/1711421463204/" onclick="doTaskLinkClick(0,4308,'你与人生赢家间差哪？','1')" target="_blank" class="noline jobLink">
                            <span id="link_4308" style="">你与人生赢家间差哪？</span></a>
                </li>

                <li id="task_item_8410" class="newtask">
                    <a class="floatright gray noline" href="http://class.hujiang.com/classzt/MKTTopic_p91454/?channel=3352&amp;ch_campaign=cls12913&amp;ch_source=isc_bulo_0_blsxhyl" onclick="doTaskLinkClick(0,8410,'什么？Kindle耳机免费送？','1')" target="_blank">
                        +1</a> <a href="http://class.hujiang.com/classzt/MKTTopic_p91454/?channel=3352&amp;ch_campaign=cls12913&amp;ch_source=isc_bulo_0_blsxhyl" onclick="doTaskLinkClick(0,8410,'什么？Kindle耳机免费送？','1')" target="_blank" class="noline jobLink">
                            <span id="link_8410" style="">什么？Kindle耳机免费送？</span></a>
                </li>

    </ul>
</div>


                    <!-- 网校公开课 -->


                    <div class="clear"></div>
                    <!-- <a href="http://t.hujiang.com/topic/%E9%9A%8F%E6%89%8B%E6%8B%8D%E6%99%92%E5%B9%B4%E5%91%B3%E5%84%BF/" title="随手拍年味儿" target="_blank"><img src="http://i1.t.hjfile.cn/ing_new/201201_3/66d371df-8d88-4923-a561-e490be512848.gif" width="250" height="129" style="margin-top:8px;" /></a> -->

                    <!--碎碎 微学习-->

<a href="http://st.hujiang.com/topic/167534262090/?ch_campaign=sc10834&amp;ch_source=isc_bulo_0_blsyyctw" target="_blank" title="社团">
    <img src="http://i3.s.7.hjfile.cn/entry/201604/635a9ba8-fc0a-4f29-93a2-f29b074d1bd0.jpg" style="padding-top:5px">
</a>


                    <div class="clear"></div>
                    <!-- 今日团购 -->
                    <div id="NewTuan_pnlTuan">

    <div id="tuan" style="width:250px;">
        <h3 class="h3_ing">
            <ul id="icons_tuan" class="fr">
                <li><a href="javascript:void(0);" class="tuan_prev fr" title="上一个" onclick="doRecord2(this,'上一个团购','部落团购');"></a></li>
                <li><a href="javascript:void(0);" class="tuan_next fr" title="下一个" onclick="doRecord2(this,'下一个团购','部落团购');"></a></li>
                <li id="pop_tuan_li"><a href="javascript:void(0);" class="tuan_more fr"></a>
                    <div class="icon_tuan hide">
                        <em class="arrow_tuan"></em>
                        <ul>
                            <li><a href="http://tuan.hujiang.com/?source=930" target="_blank" onclick="doRecord2(this,'更多团购','部落团购');">更多CC课堂</a></li>
                        </ul>
                        <a href="javascript:void(0);" onclick="CloseTuan(this);">关闭该模块</a>
                    </div>
                </li>
            </ul>
            CC课堂
        </h3>
        <div id="pnl_Tuan">
        <ul class="bxslider" style=" position:relative;">

        </ul>
        </div>
    </div>

</div>

                    <!-- 今日团购end -->

                </div>
                <div id="app_sidebar_bg">
                    <!--热门话题-->

                    <!--碎碎精华集-->

<h3 onmouseover="$('#ing_album').show();" onmouseout="$('#ing_album').hide();">
    <span id="ing_album" class="floatright" style="display: none; width: 17px; overflow: hidden; margin-right: 15px;">
        <a class="set_add" title="查看更多" href="http://st.hujiang.com/" target="_blank"></a>
    </span>推荐社团
</h3>
<div class="indent clearbox LazyLoad">

    <dl class="ob">
        <dt><a href="http://st.hujiang.com/yingshishe/" target="_blank" title="影视社">
            <img alt="影视社" id="face_2" class="pf" src="/images/spacer.gif" original="http://i3.s.7.hjfile.cn/entry/201508/c9ac691c-378b-47ed-9d1b-5581ea348ee0.jpg?imageView2/1/w/192/h/192/format/png" width="48" height="48">
        </a></dt>
        <dd>
            <a href="http://st.hujiang.com/yingshishe/" target="_blank" title="影视社">影视社 </a></dd>
    </dl>

    <dl class="ob">
        <dt><a href="http://st.hujiang.com/lcjhs/" target="_blank" title="懒虫进化社">
            <img alt="懒虫进化社" id="face_2" class="pf" src="/images/spacer.gif" original="http://i3.s.7.hjfile.cn/entry/201408/7b4318e9-9169-430e-89f8-7de5c6a4804e.jpg?imageView2/1/w/192/h/192/format/png" width="48" height="48">
        </a></dt>
        <dd>
            <a href="http://st.hujiang.com/lcjhs/" target="_blank" title="懒虫进化社">懒虫进化社 </a></dd>
    </dl>

    <dl class="ob">
        <dt><a href="http://st.hujiang.com/nceparty/" target="_blank" title="【网校】新概念同学会">
            <img alt="【网校】新概念同学会" id="face_2" class="pf" src="/images/spacer.gif" original="http://i3.s.7.hjfile.cn/entry/201412/dcd27bcb-0b0c-4bef-b2f6-ed7da9afeb30.jpg?imageView2/1/w/192/h/192/format/png" width="48" height="48">
        </a></dt>
        <dd>
            <a href="http://st.hujiang.com/nceparty/" target="_blank" title="【网校】新概念同学会">【网校】新概念同学会 </a></dd>
    </dl>

</div>

                    <!--最近访客-->

<br>
                    <!--移动互联 . 精彩学习人生-->

<style>
    .ul_close
    {
        display: none;
    }
    .ul_open
    {
        display: block;
    }
    .home_best_zone ul
    {
        width: 206px;
        height: 67px;
        overflow: hidden;
    }
</style>
<div class="home_best_zone">
    <div class="home_rt_tj">
        <span class="floatright"><a class="noline" href="http://www.hujiang.com/app/" target="_blank">
            全部»</a></span><b>移动互联 · 精彩学习人生</b></div>
    <div class="pnl_MobileApp">

                <ul class="ul_close">
                    <li class="lt"><a href="/mobile/app/57/#pnl_app57" target="_blank">
                        <img src="http://app.m.hjfile.cn/android/appImages/a_txk/ico_a_txk.png" original="http://app.m.hjfile.cn/android/appImages/a_txk/ico_a_txk.png"></a></li>
                    <li class="rt">
                        <!-- <span class="floatright"><a href="http://app.m.hjfile.cn/android/tingliku.apk" target="_blank"><img src="/app/images/ico_download.gif" /></a></span> -->
                        <a href="/mobile/app/57/#pnl_app57" target="_blank">
                            沪江听力酷</a>
                        <p class="darkgray">
                            沪江听力酷，你的掌上听力训练机！英日...
                        </p>
                    </li>
                    <div class="clear">
                    </div>
                </ul>
                <div class="clear">
                </div>

                <ul class="ul_close">
                    <li class="lt"><a href="/mobile/app/14/#pnl_app14" target="_blank">
                        <img src="http://i3.s.yun.hjfile.cn/entry/201411/50692cb4-cec8-4f70-9393-8255540d025c.png" original="http://i3.s.yun.hjfile.cn/entry/201411/50692cb4-cec8-4f70-9393-8255540d025c.png"></a></li>
                    <li class="rt">
                        <!-- <span class="floatright"><a href="http://app.m.hjfile.cn/android/HJWordGames.apk" target="_blank"><img src="/app/images/ico_download.gif" /></a></span> -->
                        <a href="/mobile/app/14/#pnl_app14" target="_blank">
                            开心词场</a>
                        <p class="darkgray">
                            背单词独门利器，采用高效的词场模式，...
                        </p>
                    </li>
                    <div class="clear">
                    </div>
                </ul>
                <div class="clear">
                </div>

                <ul class="ul_close">
                    <li class="lt"><a href="/mobile/app/11/#pnl_app11" target="_blank">
                        <img src="/app/images/spacer.gif" original="http://app.m.hjfile.cn/android/appImages/android_nce/mobile_nce_android.png"></a></li>
                    <li class="rt">
                        <!-- <span class="floatright"><a href="http://m.hujiang.com/android/nce.apk" target="_blank"><img src="/app/images/ico_download.gif" /></a></span> -->
                        <a href="/mobile/app/11/#pnl_app11" target="_blank">
                            新概念英语</a>
                        <p class="darkgray">
                            《沪江英语·新概念》安卓应用震撼推出...
                        </p>
                    </li>
                    <div class="clear">
                    </div>
                </ul>
                <div class="clear">
                </div>

                <ul class="ul_close">
                    <li class="lt"><a href="/mobile/app/5/#pnl_app5" target="_blank">
                        <img src="/app/images/spacer.gif" original="http://app.m.hjfile.cn/android/appImages/hjdict/pic_mobile_dict.gif"></a></li>
                    <li class="rt">
                        <!-- <span class="floatright"><a href="http://itunes.apple.com/cn/app/id481584414?mt=8" target="_blank"><img src="/app/images/ico_download.gif" /></a></span> -->
                        <a href="/mobile/app/5/#pnl_app5" target="_blank">
                            沪江小D</a>
                        <p class="darkgray">
                            简洁大方的界面，精选的多语种本地词库...
                        </p>
                    </li>
                    <div class="clear">
                    </div>
                </ul>
                <div class="clear">
                </div>

                <ul class="ul_close">
                    <li class="lt"><a href="/mobile/app/6/#pnl_app6" target="_blank">
                        <img src="/app/images/spacer.gif" original="http://app.m.hjfile.cn/android/appImages/tingshuodu/en/ico_hjEnNews.gif"></a></li>
                    <li class="rt">
                        <!-- <span class="floatright"><a href="http://itunes.apple.com/cn/app/id466687466?l=en&mt=8" target="_blank"><img src="/app/images/ico_download.gif" /></a></span> -->
                        <a href="/mobile/app/6/#pnl_app6" target="_blank">
                            沪江英语</a>
                        <p class="darkgray">
                            手机轻松一点，英语精彩内容立即呈现。...
                        </p>
                    </li>
                    <div class="clear">
                    </div>
                </ul>
                <div class="clear">
                </div>

                <ul class="ul_close">
                    <li class="lt"><a href="/mobile/app/4/#pnl_app4" target="_blank">
                        <img src="/app/images/spacer.gif" original="http://app.m.hjfile.cn/android/appImages/hjclass/bz/pic_mobile5.gif"></a></li>
                    <li class="rt">
                        <!-- <span class="floatright"><a href="http://m.hujiang.com/android/hujiangclass3_update2to3.apk" target="_blank"><img src="/app/images/ico_download.gif" /></a></span> -->
                        <a href="/mobile/app/4/#pnl_app4" target="_blank">
                            沪江网校</a>
                        <p class="darkgray">
                            课件下载后，可离线听课，随时随地上网...
                        </p>
                    </li>
                    <div class="clear">
                    </div>
                </ul>
                <div class="clear">
                </div>

    </div>
</div>

<script>
    $(function () {
        IniteMobileApp();
    });

</script>
                    <!--活跃用户-->

<h3>活跃用户</h3>
<div class="indent clearbox LazyLoad">

            <dl class="ob">
                <dt><a href="/3221927" target="_blank" title="judyf" class="userface" userid="3221927">
                    <img width="48" height="48" alt="judyf" class="pf" src="/images/spacer.gif" original="http://i2.hjfile.cn/f48/19/27/3221927.jpg"></a></dt>
                <dd>
                    <a href="/3221927" target="_blank" title="judyf" class="noline userface" userid="3221927">
                        judyf</a> <span><a class="gray noline" href="/3221927" target="_blank">+ 关注</a></span></dd>
            </dl>

            <dl class="ob">
                <dt><a href="/5396290" target="_blank" title="帅帅666" class="userface" userid="5396290">
                    <img width="48" height="48" alt="帅帅666" class="pf" src="/images/spacer.gif" original="http://i2.hjfile.cn/f48/62/90/5396290.jpg"></a></dt>
                <dd>
                    <a href="/5396290" target="_blank" title="帅帅666" class="noline userface" userid="5396290">
                        帅帅666</a> <span><a class="gray noline" href="/5396290" target="_blank">+ 关注</a></span></dd>
            </dl>

            <dl class="ob">
                <dt><a href="/5589794" target="_blank" title="孙杨杰" class="userface" userid="5589794">
                    <img width="48" height="48" alt="孙杨杰" class="pf" src="/images/spacer.gif" original="http://i2.hjfile.cn/f48/97/94/5589794.jpg"></a></dt>
                <dd>
                    <a href="/5589794" target="_blank" title="孙杨杰" class="noline userface" userid="5589794">
                        孙杨杰</a> <span><a class="gray noline" href="/5589794" target="_blank">+ 关注</a></span></dd>
            </dl>

            <dl class="ob">
                <dt><a href="/2212305" target="_blank" title="huoyuwang" class="userface" userid="2212305">
                    <img width="48" height="48" alt="huoyuwang" class="pf" src="/images/spacer.gif" original="http://i2.hjfile.cn/f48/23/05/2212305.jpg"></a></dt>
                <dd>
                    <a href="/2212305" target="_blank" title="huoyuwang" class="noline userface" userid="2212305">
                        huoyuwang</a> <span><a class="gray noline" href="/2212305" target="_blank">+ 关注</a></span></dd>
            </dl>


            <dl class="ob">
                <dt><a href="/19690495" target="_blank" title="Vcappuccino" class="userface" userid="19690495">
                    <img width="48" height="48" alt="Vcappuccino" class="pf" src="/images/spacer.gif" original="http://i2.hjfile.cn/f48/04/95/19690495.jpg"></a></dt>
                <dd>
                    <a href="/19690495" target="_blank" title="Vcappuccino" class="noline userface" userid="19690495">
                        Vcappuccino</a> <span><a class="gray noline" href="/19690495" target="_blank">+ 关注</a></span></dd>
            </dl>

            <dl class="ob">
                <dt><a href="/1983064" target="_blank" title="韦博国际英语" class="userface" userid="1983064">
                    <img width="48" height="48" alt="韦博国际英语" class="pf" src="/images/spacer.gif" original="http://i2.hjfile.cn/f48/30/64/1983064.jpg"></a></dt>
                <dd>
                    <a href="/1983064" target="_blank" title="韦博国际英语" class="noline userface" userid="1983064">
                        韦博国际英语</a> <span><a class="gray noline" href="/1983064" target="_blank">+ 关注</a></span></dd>
            </dl>

</div>
                    <br>
                    <br>

                </div>
            </div>"""
    my_webpage = MyWebpage(init_html)
    task_link = my_webpage.find_element_id("task_link")
    tag_li = my_webpage.find_element_tag(task_link, "li")
    list_task_id = my_webpage.get_list_info(tag_li, "id", "task_item_")
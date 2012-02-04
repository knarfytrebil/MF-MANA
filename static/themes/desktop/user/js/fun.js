// JavaScript Document
function switchTab(identify,index,count,cnon,cnout) {
    for(i=0;i<count;i++) {
        var CurTabObj = document.getElementById("Tab_"+identify+"_"+i) ;
        var CurListObj = document.getElementById("List_"+identify+"_"+i) ;
        if (i != index) {
            CurTabObj.className=cnout ;
            CurListObj.style.display="none" ;
        }
    }
    //try {
//        for (ind=0;ind<CachePic['recommend'][index].length ;ind++ ) {
//            var picobj = document.getElementById("recommend_pic_"+index+"_"+ind) ;
//            //if (picobj.src == "http://localhost/images/img_default.gif") {
//                picobj.src = CachePic['recommend'][index][ind] ;
//            //}
//        }
//    }
//    catch (e) {}
//    
    document.getElementById("Tab_"+identify+"_"+index).className=cnon ;
    document.getElementById("List_"+identify+"_"+index).style.display="";
}

//Chart switch Event 
function plot_overview(class_id,data){
    $.plot($(class_id), data, {
        series: {
            bars: { show: true },
            shadowSize: 0
        },
        grid: { color: "#999" },
        xaxis: { ticks: [], mode: "time" },
        yaxis: { ticks: [], min: 0, autoscaleMargin: 0.1 }
    });
}
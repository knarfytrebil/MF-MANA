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
    $.plot($(class_id), [data], {
        series: {
            lines: { show: true, lineWidth: 1 },
            shadowSize: 0
        },
        grid: { color: "#FFF" },
        xaxis: { ticks: [], mode: "time" },
        yaxis: { ticks: [], min: 0, autoscaleMargin: 0.1 }
    });
}

//Big Plot
function plot_big(class_id,data){
    // helper for returning the weekends in a period
    function weekendAreas(axes) {
        var markings = [];
        var d = new Date(axes.xaxis.min);
        // go to the first Saturday
        d.setUTCDate(d.getUTCDate() - ((d.getUTCDay() + 1) % 7))
        d.setUTCSeconds(0);
        d.setUTCMinutes(0);
        d.setUTCHours(0);
        var i = d.getTime();
        do {
            // when we don't set yaxis, the rectangle automatically
            // extends to infinity upwards and downwards
            markings.push({ xaxis: { from: i, to: i + 2 * 24 * 60 * 60 * 1000 } });
            i += 7 * 24 * 60 * 60 * 1000;
        } while (i < axes.xaxis.max);

        return markings;
    }

    var options = {
        xaxis: { mode: "time" },
        minTickSize: [1, "month"],
        grid: { markings: weekendAreas }
    };

    $.plot($(class_id), [data], options);
}
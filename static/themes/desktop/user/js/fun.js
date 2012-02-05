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

//Big Plot
function plot_big(class_id,data){

    var options = {
        bars: { show: true },
        points: { show: true },
        color: "rgb(255,50,50)",
        xaxis: { mode: "time" },
        grid: { 
            markings: weekendAreas,
            backgroundColor: { colors: ["#fff", "#eee"] },
            hoverable: true
        }
    };

    $.plot($(class_id), [data], options);
}


//plot hover
function showTooltip(x, y, contents) {
    $('<div id="tooltip">' + contents + '</div>').css( {
        position: 'absolute',
        display: 'none',
        top: y + 5,
        left: x + 5,
        'color' : '#FFF',
        border: '1px solid #001',
        padding: '4px',
        'background-color': '#000',
        opacity: 0.80
    }).appendTo("body").fadeIn(200);
}

function BindToolTip(plottarget) {
    var previousPoint = null;
    $(plottarget).bind("plothover", function (event, pos, item) {
        
        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;
                
                $("#tooltip").remove();
                var x = item.datapoint[0].toFixed(2),
                    y = item.datapoint[1].toFixed(2);
                
                showTooltip(item.pageX, item.pageY,
                            "流量 ＝ " + y);
            }
        }
        else {
            $("#tooltip").remove();
            previousPoint = null;            
        }
        
    });
}
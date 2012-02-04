//Chart switch Event 
function plot_overview(class_id,data){
	$.plot($(class_id), data, {
		series: {
			lines: { show: true, lineWidth: 1 },
			shadowSize: 0
		},
		grid: { color: "#999" }
	});
}
//Chart switch Event 
 $(function() {
	$('#box_3').hide();
	$('#box_4').hide();
	$('#chartdiv_2').hide();
	$('#chartdiv_4').hide();
	$('#chartdiv_6').hide();

	//box_2
	$('#ui-select-one').click(function(){
		$('#box_2').slideDown();
		$('#box_3').slideUp();
		$('#box_4').slideUp();
	});
	$('#ui-select-two').click(function(){
		$('#box_3').slideDown();
		$('#box_2').slideUp();
		$('#box_4').slideUp();
	});
	$('#ui-select-three').click(function(){
		$('#box_4').slideDown();
		$('#box_2').slideUp();
		$('#box_3').slideUp();
	});
	//chart 1
	$('#month').click(function(){
			$('#chartdiv_1').show();
			$('#chartdiv_2').hide();
		});
	$('#day').click(function(){
			$('#chartdiv_2').show();
			$('#chartdiv_1').hide();
	});
	//chart 2
	$('#month1').click(function(){
			$('#chartdiv_3').show();
			$('#chartdiv_4').hide();
		});
	$('#day1').click(function(){
			$('#chartdiv_4').show();
			$('#chartdiv_3').hide();
	});
	//chart 3
	$('#month2').click(function(){
			$('#chartdiv_5').show();
			$('#chartdiv_6').hide();
		});
	$('#day2').click(function(){
			$('#chartdiv_6').show();
			$('#chartdiv_5').hide();
	});
});



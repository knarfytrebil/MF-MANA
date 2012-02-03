$(document).ready(function() {
    $('#graphic2').hide();
	$('#day').click(function(){
			$('#graphic1').show();
			$('#graphic2').hide();
		});
	$('#month').click(function(){
		$('#graphic2').show();
		$('#graphic1').hide();
	});
});
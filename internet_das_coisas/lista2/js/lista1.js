function mudar(){
	msg = "0 - mudou<br/>";
	for (var i = 1; i<11; i++ ){
		msg = msg + i + ' - ' + 'mudou<br/>';
	}
	document.getElementById("result").innerHTML = msg;
}

function liga_lamp(){
	document.getElementById("luz1").src = "imagens/Lon.png"
}
function desliga_lamp(){
	document.getElementById("luz1").src = "imagens/Loff.png"
}

// uso de notificaciones

document.addEventListener('DOMContentLoaded', function()
{
	if(Notification.permission != 'granted')
		Notification.requestPermission();
})


function notificar(titulo, mensaje, url)
{
	if(Notification.permission != 'granted')
		Notification.requestPermission();
	else
	{
		var notificacion = new Notification(
			titulo,
			{	
				icon				: 'core/img/bob.png',
				body				: mensaje,
				requireInteraction	: false
			}
		);
		
		notificacion.onclick = function(){
			window.open(url);
		}
	}
}

setTimeout(function()
//setInterval(function()
{
	var titulo 	= "Brother ";
	var mensaje	= "Ponemos todo para romper la discoteca";
	var url		= "https://epic-panini-ad3da8.netlify.app/";//"/admin";
	notificar(titulo, mensaje, url);
}, 3000);

//NOTIFICACION TERMINADA
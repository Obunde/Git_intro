document.addEventListener('DOMContentLoaded', () => {
	const script = document.createElement('script');
	script.type = 'text/javascript';
	script.textContent = `console.log('Page script loaded');`;
	document.head.appendChild(script);
});

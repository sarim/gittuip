<style>
.value {
	background-color: rgb(83, 180, 79);
	border-bottom-left-radius: 20px;
	border-bottom-right-radius: 20px;
	border-top-left-radius: 20px;
	border-top-right-radius: 20px;
	color: rgb(255, 255, 255);
	display: inline-block;
	font-family: proxima-nova, sans-serif;
	font-size: 12px;
	font-weight: bold;
	height: 14px;
	line-height: 14.203125px;
	margin: 0.2em;
	padding: 0.35em 0.9em 0.35em;
	vertical-align: baseline;
	white-space: nowrap;
}
.key {
	background-color: rgb(77, 55, 12);
	border-bottom-left-radius: 20px;
	border-bottom-right-radius: 20px;
	border-top-left-radius: 20px;
	border-top-right-radius: 20px;
	color: rgb(255, 255, 255);
	display: inline-block;
	font-family: proxima-nova, sans-serif;
	font-size: 12px;
	font-weight: bold;
	height: 14px;
	line-height: 14.203125px;
	margin: 0.2em;
	padding: 0.35em 0.9em 0.35em;
	vertical-align: baseline;
	white-space: nowrap;
}
</style>
%for key,value in data.iteritems():
<div>
<span class="key">{{ key }}</span>
<span class="value">{{ "_None_" if value=="" else value }}</span>
</div>
%end
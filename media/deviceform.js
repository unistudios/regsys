Ext.onReady(function(){

	Ext.create('Ext.grid.Panel', {
	    renderTo: mygrid,
	    store: deviceStore,
	    height: 200,
	    title: 'Current Device List',
	    columns: [
	        {
	        	header: 'Host Name',  
	        	dataIndex: 'name',  
	        },
	        {
	            header: 'IP Address',
	            dataIndex: 'ipaddress',
	        },
	    ],
	});
});
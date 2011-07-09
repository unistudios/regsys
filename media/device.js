Ext.define('Host', {
    extend: 'Ext.data.Model',
    fields: [
    			{name:'id', mapping : 'fields.name'},
    		 	{name:'ipaddress', mapping 
    		 'ipaddress',
    		]
});

var deviceStore = Ext.create('Ext.data.Store', {
    model: 'Host',
    proxy: {
    	type : 'ajax',
    	url :  'data/',
    	reader : {
    		type: 'json',
    	}, 
    	writer : {
    		type: 'json'
    	},
    },
    autoLoad: true,
    autoSync: true,
});
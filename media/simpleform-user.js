Ext.define('User', {
    extend: 'Ext.data.Model',
    fields: [ 'name', 'email', 'phone' ]
});

var userStore = Ext.create('Ext.data.Store', {
    model: 'User',
    proxy: {
    	type : 'ajax',
    	url :  'data/users/',
    	reader : {
    		type: 'json'
    	}, 
    	writer : {
    		type: 'json'
    	},
    	
    },
    autoLoad: true,
    autoSync: true,
    
});
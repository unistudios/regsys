Ext.onReady(function(){

	Ext.create('Ext.grid.Panel', {
	    renderTo: Ext.getBody(),
	    store: userStore,
	    width: 800,
	    height: 200,
	    title: 'Application Users',
	    columns: [
	        {header: 'Name',  dataIndex: 'name',  field: 'textfield'},
	        {
	            text: 'Email Address',
	            width: 150,
	            dataIndex: 'email',
	            hidden: true
	        },
	        {
	            text: 'Phone Number',
	            flex: 1,
	            dataIndex: 'phone'
	        }
	    ],
	    selType: 'cellmodel', 
	    plugins: [
	    	Ext.create('Ext.grid.plugin.RowEditing',{
	    		clicksToEdit: 1
	    	})
	    ],
	    
	});

});

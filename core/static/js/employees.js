$('button[data-type="employees"]').one("click", function(){
    let department = this.getAttribute("data-pk")
	$.ajax({
		url: `/api/employees/department/${department}/`,
		method: 'get',
		dataType: 'json',
		data: $(this).serialize(),
		success: function(data){
            let table_html = `
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Фамилия</th>
                            <th scope="col">Имя</th>
                            <th scope="col">Отчество</th>
                            <th scope="col">Должность</th>
                            <th scope="col">Размер зарплаты</th>
                            <th scope="col">Дата приёма на работу</th>
                        </tr>
                    </thead>
            `;

            let i = 0;
            while (i < data.length) {
                table_html += `
                    <tr>
                        <th scope="col">${ i+1 }</th>
                        <th scope="col">${ data[i]["surname"] }</th>
                        <th scope="col">${ data[i]["name"] }</th>
                        <th scope="col">${ data[i]["paternal_name"] }</th>
                        <th scope="col">${ data[i]["position"] }</th>
                        <th scope="col">${ data[i]["salary_amount"] }</th>
                        <th scope="col">${ data[i]["employment_date"] }</th>
                    </tr>
                `;

                i++;
            }

            table_html +=  "</table>";

            $("#collapseEmployees_" + department + "").html(table_html);
		}
	});
});
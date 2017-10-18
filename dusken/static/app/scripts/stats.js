var saleTypes = [];
var salesData = {};

var salesChart;
var salesChartToday;

var url = '/api/stats/';

function sumSales(memo, num) {
    return memo + num.sales;
}

function toHighchartsSeries(memberships) {
    memberships = _.sortBy(memberships, 'date');
    return _.map(memberships, function (el) {
        return [moment.utc(el.date).valueOf(), el.sales]
    });
}

function getSales(start) {
    return $.getJSON(url + '?start_date=' + start, function (data) {
        salesData = data.memberships;
        saleTypes = data.payment_methods;
        _.each(saleTypes, function(type) {
            salesChart.addSeries({name: type +'-salg', data: toHighchartsSeries(salesData[type])});
        })
    });
}

function totals() {
    var sum = 0;
    _.each(saleTypes, function(type) {
        var total = _.reduce(salesData[type], sumSales, 0);
        $('.'+ type).html(total);
        sum += total;
    }) ;

    $('.sum').html(sum);
}

function today() {
    var today = moment.utc().format('YYYY-MM-DD');
    $('.today-date-wrap').text(today);
    var todaySales = _.findWhere(salesData, {date: today}) || {sales: 0};
    $('.app-today').html(todaySales.sales);

    salesChartToday = new Highcharts.Chart({
        chart: {
            renderTo: 'sales-chart-today',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: false
        },
        series: [{
            name: 'Salg', data: [
                {name: 'Salg', y: todaySales.sales},
            ]
        }
        ]
    });
}

function groupSalesByDate() {
    var salesByDate = {};
    _.each(saleTypes, function (type) {
        _.each(salesData[type], function (el) {
            var d = {};
            d[el.date] = {};
            d[el.date][type]= el.sales;

            $.extend(true, salesByDate, d);
        });
    });
    /* add zeros */
    _.each(salesByDate, function (sales, date) {
        _.each(saleTypes, function (type) {
            if(typeof sales[type] == 'undefined') {
                salesByDate[date][type] = 0;
            }
        });
    });

    var table_friendly = [];
    _.each(salesByDate, function (sales, date) {
        sales.date = date;
        table_friendly.push(sales);
    });
    table_friendly = _.sortBy(table_friendly, 'date').reverse();

    return table_friendly;
}

function salesTable() {
    var html = '<thead><tr><th>Dato</th>';
    _.each(saleTypes, function(type) {
        html += '<th>' + type + '</th>';
    });
    html += '</tr></thead><tbody>';
    salesData = groupSalesByDate();

    _.each(salesData, function(el) {
        html += '<tr><td>' + el.date + '</td>';
        _.each(saleTypes, function(type) {
            console.log(el);
            html += '<td>' + el[type] + '</td>';
        });
        html += '</tr>';
    });
    html += '</tbody>';
    $('#sales-table').html(html);
}

function toCSV(data) {
    var csvLines = data.map(function(d){
        return d.date + ',' + saleTypes.map(function(t) { return d[t]; }).join(',');
    });
    var csvHeader = 'date,' +saleTypes.join(',') + '\n';
    return csvHeader + csvLines.join('\n')
}

function downloadCSVFile(csvData, fileName) {
    csvData = 'data:text/csv;charset=utf-8,' + csvData;
    var encodedUri = encodeURI(csvData);

    var link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', fileName);
    document.body.appendChild(link); // Required for FF

    link.click();
}

function recalc(start, cb) {
    salesChart = new Highcharts.Chart({
        chart: {
            renderTo: 'sales-chart'
        },
        title: {
            text: false
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: 'Salg'
            },
            min: 0
        },
        plotOptions: {
            series: {
                marker: {
                    radius: 4
                }
            }
        },
        series: []
    });

    $.when(getSales(start)).done(function() {
        totals();
        salesTable();

        if(cb) {
            cb();
        }
    });
}

$(document).ready(function() {
    Highcharts.setOptions({
        credits: {enabled: false}
    });

    var $exportBtn = $('.export-data-btn');
    var $startInput = $('#start');

    var start = $startInput.val();
    recalc(start, function() {
        today();
    });

    /* Dynamic date change */
    $startInput.on('input', function(e) {
        start = $(e.target).val();
        history.replaceState(null, null, '?start_date=' + start);
        recalc(start);
    });

    /* Export to CSV */
    $exportBtn.on('click', function (e) {
        e.preventDefault();
        var fileName = 'medlemskapsstats-' + $startInput.val() + '.csv';
        var csvData = toCSV(salesData);
        downloadCSVFile(csvData, fileName);
    });

});

$(function () {
    $('#container1').highcharts({
        title: {
            text: 'Breast Cancer Prediction',
            x: -20 //center
        },
        subtitle: {
            text: 'Source: SEER',
            x: -20
        },
        xAxis: {
            title: {
                text: 'False Positive Rate' //yTitle //
            },
            categories: [0.0, 0.01, 0.02, 0.03, 0.04, 1.0]
        },
        yAxis: {
            title: {
                text: 'True Positive Rate' //yTitle //
            },
            // categories: [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '°C'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [ {
            name: 'Logistic Regression',
            data: [0.0, 0.2, 0.4, 0.6, 0.8, 1.0] // [0.0, 0.01, 0.02, 0.03, 0.04, 1.0]
        },{
            name: 'Patient',
            data: [0.5]
        }
        ]
    });
});

$(function () {
    $('#container4').highcharts({

        title: {
            text: 'Logarithmic axis demo'
        },

        xAxis: {
            tickInterval: 1
        },

        yAxis: {
            type: 'logarithmic',
            minorTickInterval: 0.1
        },

        tooltip: {
            headerFormat: '<b>{series.name}</b><br />',
            pointFormat: 'x = {point.x}, y = {point.y}'
        },

        series: [{
            data: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],
            pointStart: 1
        }]
    });
});

$(function () {
    $('#container2').highcharts({
        chart: {
            type: 'line'
        },
        title: {
            text: 'Sample Chart 2'
        },
        subtitle: {
            text: 'Source: WorldClimate.com'
        },
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
        yAxis: {
            title: {
                text: 'Temperature (°C)'
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        series: [{
            name: 'Tokyo',
            data: [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }, {
            name: 'London',
            data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
        }]
    });
});
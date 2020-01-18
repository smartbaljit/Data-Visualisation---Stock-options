// STEP 1: READ CSV USING JavaScript (D3.json())
d3.csv('FB.csv')
  .then(function(data) {
    console.log('data:', data);

    // STEP 2: Extract our x and y values from the CSV
    let dates = []; // get x value data
    let prices = []; // get y value data

    // Loop through records
    for (let i = 0; i < data.length; i++) {
      // convert adj.close and date to number values and append them to our empty lists
      let record = data[i];

      // EXTRACTION: add values to our empty lists
      dates.push(record['Date']);
      prices.push(+record['Adj Close']);
    }

    console.log('dates:', dates);
    console.log('prices:', prices);

    // convert adj.close and date to number values

    // STEP 3: Create the chart using the data
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: dates, // X Values
        datasets: [{
          label: 'FB',
          data: prices, // Y Values
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }]
      },
      layout: {
        padding: {
          left: 1,
          right: 1,
          top: 1,
          bottom: 1
        }
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        }
      }
    });
    
    
  })
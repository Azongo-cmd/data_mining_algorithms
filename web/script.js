
data_metric = document.getElementById('metric')
data_metric_value = document.getElementById('min-conf')

data_metric.addEventListener('change', function handleChange(event) {
    if (event.target.value == 0) {
        data_metric_value.style.display = 'flex';
    } else {
        data_metric_value.style.display = 'none';
    }
  });
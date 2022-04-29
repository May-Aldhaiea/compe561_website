var input = document.querySelector('#options-per-view-input')

var glide = new Glide('#options-per-view', {
  perView: input.value
})

input.addEventListener('input', function (event) {
  glide.update({
    perView: event.target.value
  })
})

glide.mount()
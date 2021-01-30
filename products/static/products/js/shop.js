const shopButton = document.querySelectorAll('.shop-button')
shopButton.forEach(btn => {
    const categoryName = btn.innerHTML.toLowerCase();
    btn.style.backgroundImage = `url('/media/${categoryName}-btn.png')`;
    console.log(categoryName)
});


const sort = document.getElementById('sort-trigger')
const container = document.getElementById('sort-container')

sort.addEventListener('click', function () {
    container.classList.toggle('sort-width');
});


const starRating = document.querySelectorAll('.rating-stars')
// Loop through all star rating divs and add star icons depending on the rating
starRating.forEach(rating => {
    const ratingValue = parseInt(rating.getAttribute('data-value'))
    const fullStar = ratingValue;
    const emptyStar = 5 - fullStar;
    let stars = '';

    for (let i = 1; i < 6; i++) {
        if (i <= fullStar) {
            stars += `<i class="fas fa-star"></i>`;
        }
        else {
            stars += `<i class="far fa-star"></i>`;
        }
    }    
    rating.innerHTML = stars
});
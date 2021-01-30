const shopButton = document.querySelectorAll('.shop-button')
shopButton.forEach(btn => {
    const categoryName = btn.innerHTML.toLowerCase();
    btn.style.backgroundImage = `url('/media/${categoryName}-btn.png')`;
    console.log(categoryName)
});
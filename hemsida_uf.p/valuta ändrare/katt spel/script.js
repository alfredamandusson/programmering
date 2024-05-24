const apiKey = 'YOUR_API_KEY_HERE'; 
const apiUrl = `https://api.thecatapi.com/v1/images/search?api_key=${apiKey}`;

const newCatButton = document.getElementById('new-cat');
const catImage = document.getElementById('cat-image');

async function fetchCatImage() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        catImage.src = data[0].url;
    } catch (error) {
        console.error('Error fetching cat image:', error);
    }
}

newCatButton.addEventListener('click', fetchCatImage);


fetchCatImage();

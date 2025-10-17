async function updateEmotion() {
  try {
    const res = await fetch('/get_emotion');
    const data = await res.json();

    document.getElementById('emotion').innerText = data.emotion.toUpperCase();
    const list = document.getElementById('songList');
    list.innerHTML = '';

    data.songs.forEach(song => {
      const div = document.createElement('div');
      div.classList.add('song');
      div.innerHTML = `
        <h3>${song.title}</h3>
        <p>${song.mood}</p>
        <iframe width="300" height="180"
          src="https://www.youtube.com/embed/${song.id}"
          frameborder="0" allowfullscreen></iframe>
      `;
      list.appendChild(div);
    });
  } catch (err) {
    console.error('Error fetching emotion:', err);
  }
}

setInterval(updateEmotion, 4000);

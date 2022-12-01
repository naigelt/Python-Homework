async function get Airport(icao){
  try{}
  fetch('http://localhost:5000/airport/' + icao)
} catch (error){
  console.log('Verkkovirhe', error);
}
export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }

  const values = [];

  set.forEach((value) => {
    if (value.startsWith(startString)) {
      values.push(value.slice(startString.length));
    }
  });

  return values.join('-');
}

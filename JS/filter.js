let data = [
  "files/dir1/file",
  "files/dir1/file2",
  "files/dir2/file",
  "files/dir2/file2"
];
let filteredData = data.filter(path => path.includes('dir2'));
console.log(filteredData);

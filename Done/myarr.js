class MyArr {
  constructor() {
    this.data = {};
    this.length = 0;
  }

  add(item) {
    this.data[this.length] = item;
    this.length++;
  }
  getData() {
    return Object.entries(this.data)
      .sort((a, b) => a - b)
      .map((a) => a[1]);
  }

  Map(func) {
    const entries = Object.entries(this.data);
    const outEntries = [];
    for (const e of entries) {
      outEntries.push([e[0], func(e[1])]);
    }
    this.data = Object.fromEntries(outEntries);
  }
}

arr = new MyArr();

arr.add(1);
arr.add(4);
arr.add(5);
console.log(arr.getData());
arr.Map((v) => v * 123);
console.log(arr.getData());


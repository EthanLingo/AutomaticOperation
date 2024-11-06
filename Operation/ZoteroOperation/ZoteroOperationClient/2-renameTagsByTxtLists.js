// //NOTE 这个是可以使用的。强烈推荐用这个方案批量更改标签！
// //WARNING 警告：运行任何代码之前，请先备份您的 Zotero 数据库！
// --------------- 方案 2 ---------------
// 以前自己写的代码，不记得做什么了。现在让 AI 帮我解读一下 ---------------
// 这段 JavaScript 代码的主要目的是在 Zotero（一个引用管理软件）中批量重命名标签（tag）。这个过程分为几个步骤：
// 首先，定义了一些变量，包括要搜索的字段名称（field_name）、搜索条件（condition）和标签的类型（num）。
// 然后，从 tags_txt 中获取标签列表，并将其解析成 JSON 对象。
// 接着，遍历标签列表，对每一个标签进行如下操作：
// 获取旧标签名称（name_tag_old）和新标签名称（name_tag_new）。
// 创建一个新的 Zotero 搜索对象（zotero_search），并设置其 libraryID 为当前选中的库的 ID。
// 使用 addCondition 方法添加搜索条件。这里的条件是标签字段（tag）包含旧标签名称（name_tag_old）。
// 执行搜索并获取搜索结果的 ID（id_items）。如果没有找到任何项目，函数将返回 "No items found"。
// 如果找到了符合条件的项目，那么将获取这些项目的详细信息（items）。
// 在一个数据库事务中，遍历每一个项目，移除旧的标签，添加新的标签，并保存这个更改。这里使用了 Zotero.DB.executeTransaction 方法来确保所有的更改都在一个数据库事务中完成，这样可以保证数据的一致性。
// 最后，返回一个消息，告知用户有多少个标签被更新了。
// 这段代码的主要应用场景可能是在 Zotero 中批量更新标签名称。例如，如果你想将所有标签为 "统计学习" 的项目的标签改为 "【内容】：统计学习"，那么这段代码就可以帮助你完成这个任务。

// 从 tags_txt 中获取标签列表
const tags_txt = `
// 请在此处粘贴标签列表
// 举例：
文献/综述
文献/手册
`;

const tagList = tags_txt.trim().split('\n').map(line => {
  const regex = /^(?!#)(.*)\/(.*)/;  // 这里是你需要设置的正则表达式
  const match = line.match(regex);
  if (match) {
    return [match[0], `#${match[1]}/${match[2]}`];  // 这里是你需要设置的新标签名称
  } else {
    return [line, line];
  }
});

//// 以下是正文
var count_tag_updated = 0;
var field_name = 'tag';
var condition = 'contains';
var num = 0; // num=0是手动，num=1是自动。
// 解析成json对象
list_tags = tagList;
// 遍历tag列表
for (let i in list_tags) {
  name_tag_old = list_tags[i][0];
  name_tag_new = list_tags[i][1];

  //// 以下操作Zotero
  let zotero_search = new Zotero.Search();
  zotero_search.libraryID = ZoteroPane.getSelectedLibraryID();
  zotero_search.addCondition(field_name, condition, name_tag_old);
  var id_items = await zotero_search.search();
  if (!id_items.length) {
    return "No items found";
  }
  items = Zotero.Items.get(id_items);
  await Zotero.DB.executeTransaction(async function () {
    for (let item of items) {
      item.removeTag(name_tag_old)
      item.addTag(name_tag_new, num);
      await item.save({
        skipDateModifiedUpdate: true
      });
    }
  });
  // 计数已经重命名的tag个数
  count_tag_updated += 1;
}
return count_tag_updated + " tags updated.";







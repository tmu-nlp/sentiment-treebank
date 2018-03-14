class Node():
    def __init__(self):
        self.num = 0
        self.parent = None # 親
        self.children = [] # 子のリスト

class Tree():
    def __init__(self):
        self.idx = 1
        self.root = Node()
        self.nums =  []
    
    def txt_to_tree(self, txt, parent = None):
        for c in txt:
            if c not in '()':
                continue
            elif c == '(':
                # '('が来たらノードを作って一つ潜る
                if not parent:
                    parent = Node()
                    self.root = parent
                    continue
                
                new_node = Node()
                # 親更新
                new_node.parent = parent
                # 作成ノードを親の子に追加
                parent.children.append(new_node) 
                # 親を作成ノードに更新 
                parent = new_node
            else:
                # ')'が来たら1つ上がる
                if parent:
                    parent = parent.parent

    def numbering(self):
        self.terminal_numbering(self.root)
        self.nonterminal_numbering(self.root)
    
    def terminal_numbering(self, node):
        if not node.children:
            node.num = self.idx
            self.idx += 1
            return
        for child in node.children:
            self.terminal_numbering(child)
        
    def nonterminal_numbering(self,node):
        # 後順
        if not node.children:
            return
        for child in node.children:
            self.nonterminal_numbering(child)
        if node.num == 0:
            node.num = self.idx
            self.idx += 1
    
    def print_nums(self):
        self.terminal_printing(self.root)
        self.nonterminal_printing(self.root)
    
    def terminal_printing(self, node):
        if not node.children:
            self.nums.append(node.parent.num)
            return
        for child in node.children:
            self.terminal_printing(child)
    
    def nonterminal_printing(self, node):
        if not node.children:
            return
        for child in node.children:
            self.nonterminal_printing(child)
        if(node != self.root):
            self.nums.append(node.parent.num)
        else:
            self.nums.append(0)
            self.nums.append("\n")

if __name__ == "__main__":
    with open('tsukuba_corpus_cky.txt','r',encoding='utf-8') as file:
        with open('STree_tsukuba.txt','w',encoding='utf-8') as file2:
            line = file.readline()
            while line:
                tree = Tree()
                tree.txt_to_tree(line)
                tree.numbering()
                tree.print_nums()
                file2.write('|'.join(map(str,tree.nums)))
                line = file.readline()

/**
 * md-toc.js v1.0.2
 * https://github.com/yijian166/md-toc.js
 */

(function(window){
    function Toc(id,options){
        this.el = document.getElementById(id);
        if(!this.el) return;
        this.options = options || {};
        this.tocLevel = parseInt(options.level) || 0;
        this.tocClass = options['class'] || 'toc';
        this.tocClass2 = options['class2'] || 'toc';
        this.tocTop = parseInt(options.top) || 0;
        this.elChilds = this.el.children;
        if(!this.elChilds.length) return;
        this._init();
    }

    Toc.prototype._init = function(){
        this._collectTitleElements();
        this._createTocContent();
        this._showToc();
    };


    Toc.prototype._collectTitleElements = function() {
        this._elTitlesNames = [],
            this.elTitleElements = [];
        for(var i=1;i<7;i++){
            if(this.el.getElementsByTagName('h'+i).length){
                this._elTitlesNames.push('h'+i);
            }
        }

        this._elTitlesNames.length = this._elTitlesNames.length > this.tocLevel ? this.tocLevel : this._elTitlesNames.length;

        for(var j=0;j < this.elChilds.length;j++){
            this._elChildName = this.elChilds[j].tagName.toLowerCase();
            if(this._elTitlesNames.toString().match( this._elChildName)){
                this.elTitleElements.push(this.elChilds[j]);
            }
        }
    };

    Toc.prototype._createTocContent = function(){
        this._elTitleElementsLen = this.elTitleElements.length;
        if(!this._elTitleElementsLen) return;
        this.tocContent = '';
        this._tempLists = [];

        // 本页面的完整地址，某些情况下base标签和页面地址不一致，会造成锚点混乱
        var url = location.origin+location.pathname;
        for(var i=0;i< this._elTitleElementsLen;i++){
            var j= i + 1;
            this._elTitleElement = this.elTitleElements[i];
            this._elTitleElementName = this._elTitleElement.tagName;
            this._elTitleElementText = this._elTitleElement.innerHTML;
            this._elTitleElement.setAttribute('id', 'tip' + i );

            this.tocContent += '<li><a href="'+ url + '#tip' + i +'">' +  this._elTitleElementText + '</a>';

            if(j != this._elTitleElementsLen){
                this._elNextTitleElementName = this.elTitleElements[j].tagName;
                if(this._elTitleElementName != this._elNextTitleElementName){
                    var checkColse = false, y = 1;
                    for(var t = this._tempLists.length - 1 ;t >= 0 ;t--) {
                        if ( this._tempLists[t].tagName == this._elNextTitleElementName){
                            checkColse = true;
                            break;
                        }
                        y++;
                    }

                    if(checkColse){
                        this.tocContent += new Array(y+1).join('</li></ul>');
                        this._tempLists.length = this._tempLists.length - y ;//更新栈的长度。
                    } else {
                        this._tempLists.push(this._elTitleElement);
                        this.tocContent += '<ul>';
                    }
                }
                else{
                    this.tocContent  += '</li>';
                }
            }else{
                if(this._tempLists.length){
                    this.tocContent += new Array(this._tempLists.length+1).join('</li></ul>');
                }else{
                    this.tocContent  += '</li>';
                }
            }
        }
        this.tocContent = '<ul>'+ this.tocContent + '</ul>';
    };

    Toc.prototype._showToc = function() {

        this.toc = document.createElement('div');
        this.toc.innerHTML = this.tocContent || '';
        this.toc.setAttribute('class',this.tocClass);
        
        this.toc2 = document.createElement('div');
        this.toc2.innerHTML = this.tocContent || '';
        this.toc2.setAttribute('class',this.tocClass2);
        if(! this.options.targetId){
            // 没有传入目标id，追加到生成目录的div内
            this.el.appendChild(this.toc);
        }else{
            //有传入目标id，直接在目标id内生成div
            document.getElementById(this.options.targetId2).appendChild(this.toc2);
            document.getElementById(this.options.targetId).appendChild(this.toc);
        }

    };

    window.Toc = Toc;

})(window);
/**
 * Consistent item heights in shelf.
 */
(function (window, $) {

  function setItemHeights (container, items, adjustChild, adjustProp) {
    var self = this;

    self.adjustItems = function (items, targetHeight, adjustChild, adjustProp) {
      adjustProp = adjustProp || 'height';
      $(items).each(function(){
        var $item = $(this)
          , $adjust = adjustChild ? $item.find(adjustChild) : $item
          , height = $item.height()
          , diff = targetHeight - height;
        if (diff > 0) {
          $adjust.css(adjustProp, adjustProp.indexOf('height') === -1 ? '+=' + diff : targetHeight);
        }
      });
    };

    $(container).each(function(){
      var $container = $(this)
        , $items = $container.find(items)
        , $row = $()
        , rowHeight = 0
        , lastOffsetTop
        , offsetTop
        , $item
        , $adjust;
      $items.each(function(){
        $item = $(this);
        $adjust = adjustChild ? $item.find(adjustChild) : $item;
        $adjust.css(adjustProp, '');
        offsetTop = $item.offset().top;
        if (lastOffsetTop !== null && offsetTop > lastOffsetTop) {
          self.adjustItems($row, rowHeight, adjustChild, adjustProp);
          rowHeight = 0;
          $row = $();
        }
        rowHeight = Math.max(rowHeight, $item.height());
        lastOffsetTop = offsetTop;
        $row = $row.add($item);
      });
      if ($row.length) {
        self.adjustItems($row, rowHeight, adjustChild, adjustProp);
      }
    });
  }

  function setItemHeightHandler () {
    setItemHeights('.shelf-small', '.item', '.item__controls', 'padding-top');
  }

  $(window)
    .on('load.itemHeights', setItemHeightHandler)
    .on('resize.itemHeights', setItemHeightHandler);

      /* Enable item height adjustments for shelves */

    $('.shelf-small').itemHeights({
      itemSelector: '.item',
      adjust:       '.item__controls',
      adjustProp:   'padding-top'
    });

}(this, jQuery));
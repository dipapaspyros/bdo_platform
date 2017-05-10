/**
 * Created by dimitris on 4/5/2017.
 */

var QueryDesigner = function($container, params) {
    var that = this;
    this.config = $.extend({}, {

        // dataset selection & options
        datasetSelect: {
            title: 'Dataset',
            source: {type: 'GET', from: '/queries/datasets/'}
        },

        // toolbar
        toolbar: {
            classesSource: {type: 'GET', from: '/queries/datasets/{{ datasetId }}/variables/?p={{ p }}'}
        },

        // classes
        classes: {
            propertySource: {type: 'GET', from: '/queries/datasets/{{ datasetId }}/variables/{{ variableId }}/properties/'},
            valuesCountSource: {type: 'GET', from: '/queries/datasets/{{ datasetId }}/variables/{{ variableId }}/count/'}
        }

    }, params);

    // create the dataset select
    this.datasetSelect = new DatasetSelect(this);

    // store the container
    this.$container = $container;

    this.ui = {
        render: function() {
            // remove everything
            $container.empty();

            // add toolbar
            $container.append(
                $('<div class="toolbar-container" />')
                    .append($('<div class="toolbar" />')
                        .append(that.datasetSelect.ui.$elem)
                        .append(
                            $('<input type="search" placeholder="Search" class="form-control"/>')
                        )
                        .append(
                            $('<div class="active-classes"><span>Choose a data source to explore</span></div>')
                        )
                    )
            );

            // add main region
            $container.append(
                $('<div id="builder_workspace" />')
                    .append($('<span class="help-prompt">Drag and drop items here to create a query</span>'))
                    .append($('<canvas id="builder-canvas" />'))
            );

            // resize canvas & init arrows
            $container.find("#builder-canvas").attr({
                'width': $container.find("#builder_workspace").width(),
                'height': $container.find("#builder_workspace").height()
            });
            that.arrows.set_canvas("builder-canvas");
        }
    };

    // create arrows
    this.arrows = new Arrows(this);

    // render
    this.ui.render();

    // setup toolbar
    this.toolbar = new Toolbar(this);

    // setup workbench
    this.workbench = new BuilderWorkbench(this);

    // add filters
    this.filters = new BuilderWorkbenchFilters(this);

    // add query editor
    this.editor = new QueryEditor(this);

    return this;
};

$.fn.qd = function(params) {
    QueryDesigner(this, params);

    return this
};
#!/usr/bin/env python3
"""
System Map Pipeline - Complete File System Visualization Generator
Author: Leonardo Lech
Created: 2025-07-24
Purpose: Automated file system scanning and visualization generation
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import argparse
import logging

# ==============================================================================
# PURPOSE: CONFIGURATION SECTION
# AI_EDIT_POINT: Modify these constants to customize scanning behavior
# ==============================================================================

class Config:
    """
    PURPOSE: Central configuration for system scanning and visualization
    AI_CONTEXT: All customizable parameters are defined here
    """
    
    # Directories to exclude from scanning
    EXCLUDE_DIRS = {
        '.git', '.cache', 'node_modules', '__pycache__', '.pytest_cache',
        'venv', 'env', '.env', '.venv', 'Library', '.Trash', 
        'Applications', 'Pictures', 'Movies', 'Music'
    }
    
    # File patterns to exclude
    EXCLUDE_PATTERNS = {
        '*.pyc', '*.pyo', '.DS_Store', '*.swp', '*.swo'
    }
    
    # Size thresholds (in MB)
    MIN_SIZE_TO_REPORT = 0.1  # Minimum size to include in visualization
    
    # Visualization colors (AI_EDIT_POINT: Customize color scheme)
    COLORS = {
        'projects': '#F687B3',
        'knowledge': '#63B3ED',
        'tools': '#68D391',
        'assets': '#F6E05E',
        'development': '#B794F4',
        'config': '#F6AD55',
        'temp': '#FED7AA',
        'other': '#718096'
    }
    
    # Category detection patterns (AI_EDIT_POINT: Add custom patterns)
    CATEGORY_PATTERNS = {
        'projects': ['project', 'app', 'site', 'client', 'server'],
        'knowledge': ['knowledge', 'docs', 'wiki', 'notes', 'learning'],
        'tools': ['tools', 'utils', 'scripts', 'automation'],
        'assets': ['assets', 'images', 'media', 'resources'],
        'development': ['dev', 'development', 'code', 'src'],
        'config': ['.', 'config', 'settings', 'preferences'],
        'temp': ['temp', 'tmp', 'cache', 'inbox', 'downloads']
    }

# ==============================================================================
# PURPOSE: FILE SYSTEM SCANNER MODULE
# AI_CONTEXT: Handles recursive directory scanning and size calculation
# ==============================================================================

class FileSystemScanner:
    """
    PURPOSE: Scan file system and collect directory information
    AI_CONTEXT: Main scanning logic with size calculation and categorization
    """
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.logger = logging.getLogger(__name__)
        
    def scan_directory(self, path: str, max_depth: int = 3) -> Dict:
        """
        PURPOSE: Recursively scan directory and build tree structure
        AI_CONTEXT: Returns nested dictionary with size, count, and category info
        
        Args:
            path: Root directory to scan
            max_depth: Maximum recursion depth
            
        Returns:
            Dict with directory structure and metadata
        """
        self.logger.info(f"Starting scan of {path}")
        return self._scan_recursive(Path(path), 0, max_depth)
    
    def _scan_recursive(self, path: Path, current_depth: int, max_depth: int) -> Dict:
        """
        PURPOSE: Internal recursive scanning method
        AI_CONTEXT: Handles the actual directory traversal
        """
        if not path.exists() or not path.is_dir():
            return None
            
        # Skip excluded directories
        if path.name in self.config.EXCLUDE_DIRS:
            return None
            
        dir_info = {
            'name': path.name,
            'path': str(path),
            'size': 0,
            'file_count': 0,
            'children': [],
            'category': self._determine_category(path.name),
            'color': None
        }
        
        try:
            # Calculate size and count files
            for item in path.iterdir():
                if item.is_file() and not self._should_exclude_file(item):
                    try:
                        size = item.stat().st_size / (1024 * 1024)  # Convert to MB
                        dir_info['size'] += size
                        dir_info['file_count'] += 1
                    except:
                        pass
                        
                elif item.is_dir() and current_depth < max_depth:
                    child_info = self._scan_recursive(item, current_depth + 1, max_depth)
                    if child_info and child_info['size'] >= self.config.MIN_SIZE_TO_REPORT:
                        dir_info['children'].append(child_info)
                        dir_info['size'] += child_info['size']
                        dir_info['file_count'] += child_info['file_count']
                        
        except PermissionError:
            self.logger.warning(f"Permission denied: {path}")
            
        # Set color based on category
        dir_info['color'] = self.config.COLORS.get(dir_info['category'], self.config.COLORS['other'])
        
        return dir_info
    
    def _should_exclude_file(self, file_path: Path) -> bool:
        """
        PURPOSE: Check if file should be excluded from scanning
        AI_CONTEXT: Uses exclude patterns from config
        """
        for pattern in self.config.EXCLUDE_PATTERNS:
            if file_path.match(pattern):
                return True
        return False
    
    def _determine_category(self, name: str) -> str:
        """
        PURPOSE: Determine category based on directory name
        AI_CONTEXT: Uses pattern matching from config
        """
        name_lower = name.lower()
        
        # Check each category's patterns
        for category, patterns in self.config.CATEGORY_PATTERNS.items():
            for pattern in patterns:
                if pattern in name_lower:
                    return category
                    
        # Special case for hidden directories
        if name.startswith('.'):
            return 'config'
            
        # Special case for numbered directories
        if name.startswith(('01', '02', '03', '04', '05', '99')):
            if '01' in name:
                return 'projects'
            elif '02' in name:
                return 'knowledge'
            elif '03' in name or '04' in name:
                return 'tools'
            elif '05' in name:
                return 'assets'
            elif '99' in name:
                return 'temp'
                
        return 'other'

# ==============================================================================
# PURPOSE: DATA PROCESSING MODULE
# AI_CONTEXT: Transforms raw scan data into visualization-ready format
# ==============================================================================

class DataProcessor:
    """
    PURPOSE: Process scanned data for visualization
    AI_CONTEXT: Handles data transformation and aggregation
    """
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def process_scan_data(self, scan_data: Dict) -> Dict:
        """
        PURPOSE: Transform raw scan data into visualization format
        AI_CONTEXT: Creates data structures for charts and graphs
        """
        processed = {
            'total_size': scan_data['size'],
            'total_files': scan_data['file_count'],
            'scan_date': datetime.now().isoformat(),
            'categories': self._aggregate_by_category(scan_data),
            'top_directories': self._get_top_directories(scan_data),
            'tree_data': self._prepare_tree_data(scan_data),
            'network_data': self._prepare_network_data(scan_data)
        }
        
        return processed
    
    def _aggregate_by_category(self, data: Dict) -> Dict:
        """
        PURPOSE: Aggregate sizes by category for pie chart
        AI_CONTEXT: Returns category -> size mapping
        """
        categories = {}
        
        def aggregate_recursive(node):
            category = node['category']
            if category not in categories:
                categories[category] = {'size': 0, 'count': 0, 'color': node['color']}
            categories[category]['size'] += node['size']
            categories[category]['count'] += node['file_count']
            
            for child in node.get('children', []):
                aggregate_recursive(child)
                
        aggregate_recursive(data)
        return categories
    
    def _get_top_directories(self, data: Dict, limit: int = 10) -> List[Dict]:
        """
        PURPOSE: Get largest directories for bar chart
        AI_CONTEXT: Returns sorted list of top directories by size
        """
        all_dirs = []
        
        def collect_dirs(node, level=0):
            if level <= 2:  # Only collect top-level directories
                all_dirs.append({
                    'name': node['name'],
                    'size': node['size'],
                    'category': node['category'],
                    'color': node['color']
                })
            for child in node.get('children', []):
                collect_dirs(child, level + 1)
                
        collect_dirs(data)
        return sorted(all_dirs, key=lambda x: x['size'], reverse=True)[:limit]
    
    def _prepare_tree_data(self, data: Dict) -> Dict:
        """
        PURPOSE: Prepare data for D3 treemap visualization
        AI_CONTEXT: Converts to D3-compatible format
        """
        def convert_node(node):
            return {
                'name': node['name'],
                'value': node['size'],
                'count': node['file_count'],
                'color': node['color'],
                'children': [convert_node(child) for child in node.get('children', [])]
            }
            
        return convert_node(data)
    
    def _prepare_network_data(self, data: Dict) -> Dict:
        """
        PURPOSE: Prepare data for network visualization
        AI_CONTEXT: Creates nodes and edges for vis.js
        """
        nodes = []
        edges = []
        node_id = 0
        
        def create_network(node, parent_id=None, level=0):
            nonlocal node_id
            current_id = node_id
            node_id += 1
            
            # Create node
            nodes.append({
                'id': current_id,
                'label': f"{node['name']}\\n{self._format_size(node['size'])}",
                'size': min(50, max(20, node['size'] / 100)),  # Scale size
                'color': node['color'],
                'level': level
            })
            
            # Create edge to parent
            if parent_id is not None:
                edges.append({
                    'from': parent_id,
                    'to': current_id,
                    'width': min(5, max(1, node['size'] / 1000))
                })
            
            # Process children
            for child in node.get('children', []):
                create_network(child, current_id, level + 1)
                
        create_network(data)
        return {'nodes': nodes, 'edges': edges}
    
    def _format_size(self, size_mb: float) -> str:
        """
        PURPOSE: Format size for display
        AI_CONTEXT: Converts MB to human-readable format
        """
        if size_mb >= 1000:
            return f"{size_mb / 1000:.1f}GB"
        return f"{size_mb:.0f}MB"

# ==============================================================================
# PURPOSE: HTML GENERATOR MODULE
# AI_CONTEXT: Creates the final HTML visualization file
# ==============================================================================

class HTMLGenerator:
    """
    PURPOSE: Generate HTML visualization from processed data
    AI_CONTEXT: Creates complete HTML file with embedded visualizations
    """
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        
    def generate_html(self, data: Dict, output_path: str) -> str:
        """
        PURPOSE: Generate complete HTML visualization file
        AI_CONTEXT: Main method that creates the final output
        """
        html_content = self._generate_html_template(data)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        return output_path
    
    def _generate_html_template(self, data: Dict) -> str:
        """
        PURPOSE: Generate the HTML template with embedded data
        AI_CONTEXT: This is the main HTML structure - edit styles here
        """
        # Convert data to JSON for embedding
        categories_data = json.dumps(data['categories'])
        top_dirs_data = json.dumps(data['top_directories'])
        tree_data = json.dumps(data['tree_data'])
        network_data = json.dumps(data['network_data'])
        
        # Format scan info
        total_size_gb = data['total_size'] / 1000
        scan_date = datetime.fromisoformat(data['scan_date']).strftime('%Y-%m-%d %H:%M')
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Map Visualization - Generated {scan_date}</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vis-network@latest/standalone/umd/vis-network.min.js"></script>
    <style>
        /* AI_EDIT_POINT: Modify styles here */
        body {{
            background-color: #0F1419;
            color: #E2E8F0;
            font-family: 'Inter', system-ui, sans-serif;
            margin: 0;
            padding: 0;
        }}
        
        .header {{
            background-color: #1A202C;
            padding: 20px;
            text-align: center;
            border-bottom: 3px solid #2D3748;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
        }}
        
        h1 {{
            color: #F7FAFC;
            margin: 0;
            font-size: 2.5em;
        }}
        
        .subtitle {{
            color: #CBD5E0;
            margin-top: 10px;
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
        }}
        
        .stat-item {{
            background-color: #2D3748;
            padding: 10px 20px;
            border-radius: 8px;
            border: 2px solid #4A5568;
        }}
        
        .stat-value {{
            font-size: 1.5em;
            font-weight: bold;
            color: #B794F4;
        }}
        
        .tabs {{
            background-color: #2D3748;
            padding: 0;
            margin: 0;
            display: flex;
            justify-content: center;
            border-bottom: 3px solid #4A5568;
        }}
        
        .tab-button {{
            background: none;
            color: #CBD5E0;
            border: none;
            padding: 15px 30px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
            margin: 0 5px;
        }}
        
        .tab-button:hover {{
            color: #F7FAFC;
            background-color: #374151;
        }}
        
        .tab-button.active {{
            color: #F7FAFC;
            background-color: #4A5568;
            border-bottom: 3px solid #B794F4;
        }}
        
        .tab-content {{
            display: none;
            padding: 20px;
            animation: fadeIn 0.5s;
        }}
        
        .tab-content.active {{
            display: block;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .visualization-container {{
            background-color: #1A202C;
            border: 3px solid #2D3748;
            border-radius: 12px;
            padding: 20px;
            margin: 20px auto;
            max-width: 1400px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.6);
        }}
        
        h2 {{
            color: #F7FAFC;
            text-align: center;
            margin-top: 30px;
        }}
        
        .chart-container {{
            position: relative;
            height: 400px;
            margin: 20px 0;
        }}
        
        #treemap {{
            width: 100%;
            height: 600px;
            background-color: #1A202C;
            border-radius: 8px;
            overflow: hidden;
        }}
        
        #network {{
            width: 100%;
            height: 700px;
            background-color: #1A202C;
            border-radius: 8px;
        }}
        
        button {{
            background: #B794F4;
            color: #1A202C;
            border: none;
            padding: 10px 20px;
            margin: 0 5px;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }}
        
        button:hover {{
            background: #D6B4FC;
            transform: translateY(-2px);
        }}
        
        .tooltip {{
            position: absolute;
            text-align: center;
            padding: 8px;
            font-size: 14px;
            background: #2D3748;
            color: #F7FAFC;
            border: 2px solid #B794F4;
            border-radius: 8px;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        
        .controls {{
            text-align: center;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🗂️ System Map Visualization</h1>
        <p class="subtitle">Automated File System Analysis</p>
        <div class="stats">
            <div class="stat-item">
                <div>Total Size</div>
                <div class="stat-value">{total_size_gb:.1f} GB</div>
            </div>
            <div class="stat-item">
                <div>Total Files</div>
                <div class="stat-value">{data['total_files']:,}</div>
            </div>
            <div class="stat-item">
                <div>Scan Date</div>
                <div class="stat-value">{scan_date}</div>
            </div>
        </div>
    </div>
    
    <div class="tabs">
        <button class="tab-button active" onclick="showTab('overview')">📊 Overview</button>
        <button class="tab-button" onclick="showTab('treemap')">🗺️ Treemap</button>
        <button class="tab-button" onclick="showTab('network')">🌐 Network</button>
    </div>
    
    <!-- Overview Tab -->
    <div id="overview" class="tab-content active">
        <div class="visualization-container">
            <h2>💾 Storage Distribution by Category</h2>
            <div class="chart-container">
                <canvas id="categoryChart"></canvas>
            </div>
        </div>
        
        <div class="visualization-container">
            <h2>📈 Top Directories by Size</h2>
            <div class="chart-container">
                <canvas id="topDirsChart"></canvas>
            </div>
        </div>
    </div>
    
    <!-- Treemap Tab -->
    <div id="treemap-tab" class="tab-content">
        <div class="visualization-container">
            <h2>📊 Interactive File System Treemap</h2>
            <div class="controls">
                <button onclick="updateView('size')">View by Size</button>
                <button onclick="updateView('count')">View by File Count</button>
                <button onclick="zoomOut()">Reset Zoom</button>
            </div>
            <div id="treemap"></div>
            <div class="tooltip"></div>
        </div>
    </div>
    
    <!-- Network Tab -->
    <div id="network-tab" class="tab-content">
        <div class="visualization-container">
            <h2>🌐 Directory Network Visualization</h2>
            <div id="network"></div>
        </div>
    </div>

    <script>
        // Embedded data
        const categoriesData = {categories_data};
        const topDirsData = {top_dirs_data};
        const treeData = {tree_data};
        const networkData = {network_data};
        
        // Tab functionality
        function showTab(tabName) {{
            document.querySelectorAll('.tab-content').forEach(tab => {{
                tab.classList.remove('active');
            }});
            
            document.querySelectorAll('.tab-button').forEach(button => {{
                button.classList.remove('active');
            }});
            
            if (tabName === 'overview') {{
                document.getElementById('overview').classList.add('active');
                initCharts();
            }} else if (tabName === 'treemap') {{
                document.getElementById('treemap-tab').classList.add('active');
                initTreemap();
            }} else if (tabName === 'network') {{
                document.getElementById('network-tab').classList.add('active');
                initNetwork();
            }}
            
            event.target.classList.add('active');
        }}
        
        // Initialize charts
        let chartsInitialized = false;
        function initCharts() {{
            if (chartsInitialized) return;
            chartsInitialized = true;
            
            // Category pie chart
            const categoryCtx = document.getElementById('categoryChart').getContext('2d');
            const categoryLabels = Object.keys(categoriesData).map(k => 
                k + ' (' + (categoriesData[k].size / 1000).toFixed(1) + ' GB)'
            );
            const categoryValues = Object.keys(categoriesData).map(k => categoriesData[k].size);
            const categoryColors = Object.keys(categoriesData).map(k => categoriesData[k].color);
            
            new Chart(categoryCtx, {{
                type: 'doughnut',
                data: {{
                    labels: categoryLabels,
                    datasets: [{{
                        data: categoryValues,
                        backgroundColor: categoryColors,
                        borderColor: '#1A202C',
                        borderWidth: 3
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'right',
                            labels: {{
                                color: '#E2E8F0',
                                font: {{ size: 14 }}
                            }}
                        }}
                    }}
                }}
            }});
            
            // Top directories bar chart
            const topDirsCtx = document.getElementById('topDirsChart').getContext('2d');
            new Chart(topDirsCtx, {{
                type: 'bar',
                data: {{
                    labels: topDirsData.map(d => d.name),
                    datasets: [{{
                        label: 'Size in MB',
                        data: topDirsData.map(d => d.size),
                        backgroundColor: topDirsData.map(d => d.color),
                        borderColor: '#2D3748',
                        borderWidth: 2
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            grid: {{ color: '#2D3748' }},
                            ticks: {{ color: '#E2E8F0' }}
                        }},
                        x: {{
                            grid: {{ color: '#2D3748' }},
                            ticks: {{ color: '#E2E8F0' }}
                        }}
                    }},
                    plugins: {{
                        legend: {{ display: false }}
                    }}
                }}
            }});
        }}
        
        // Treemap functionality
        let treemapInitialized = false;
        let currentView = 'size';
        let g, tooltip;
        
        function initTreemap() {{
            if (treemapInitialized) return;
            treemapInitialized = true;
            
            const width = document.getElementById('treemap').offsetWidth;
            const height = 600;
            
            const svg = d3.select("#treemap")
                .append("svg")
                .attr("width", width)
                .attr("height", height);
                
            g = svg.append("g");
            tooltip = d3.select(".tooltip");
            
            updateTreemap();
        }}
        
        function updateTreemap() {{
            const width = document.getElementById('treemap').offsetWidth;
            const height = 600;
            
            const treemap = d3.treemap()
                .size([width, height])
                .padding(2)
                .round(true);
                
            const root = d3.hierarchy(treeData)
                .sum(d => currentView === 'size' ? d.value : d.count)
                .sort((a, b) => b.value - a.value);
                
            treemap(root);
            
            const nodes = root.descendants();
            
            g.selectAll(".node").remove();
            
            const node = g.selectAll(".node")
                .data(nodes)
                .enter().append("g")
                .attr("class", "node")
                .attr("transform", d => `translate(${{d.x0}},${{d.y0}})`);
                
            node.append("rect")
                .attr("width", d => d.x1 - d.x0)
                .attr("height", d => d.y1 - d.y0)
                .attr("fill", d => d.data.color || "#718096")
                .attr("stroke", "#1A202C")
                .attr("stroke-width", 1)
                .style("cursor", d => d.children ? "pointer" : "default")
                .on("click", (event, d) => {{
                    if (d.children) zoom(d);
                }})
                .on("mouseover", (event, d) => {{
                    tooltip.transition().duration(200).style("opacity", .9);
                    tooltip.html(`<strong>${{d.data.name}}</strong><br/>Size: ${{formatSize(d.data.value)}}<br/>Files: ${{d.data.count || 'N/A'}}`)
                        .style("left", (event.pageX + 10) + "px")
                        .style("top", (event.pageY - 28) + "px");
                }})
                .on("mouseout", () => {{
                    tooltip.transition().duration(500).style("opacity", 0);
                }});
                
            node.append("text")
                .attr("x", 5)
                .attr("y", 20)
                .text(d => {{
                    const width = d.x1 - d.x0;
                    return width > 60 ? d.data.name : "";
                }})
                .attr("font-size", "14px")
                .attr("fill", "#F7FAFC")
                .style("pointer-events", "none");
        }}
        
        function zoom(d) {{
            const width = document.getElementById('treemap').offsetWidth;
            const height = 600;
            
            const x0 = d.x0, y0 = d.y0, x1 = d.x1, y1 = d.y1;
            const xScale = width / (x1 - x0);
            const yScale = height / (y1 - y0);
            
            g.transition()
                .duration(750)
                .attr("transform", `translate(${{-x0 * xScale}},${{-y0 * yScale}}) scale(${{xScale}},${{yScale}})`);
        }}
        
        function zoomOut() {{
            g.transition().duration(750).attr("transform", "translate(0,0) scale(1,1)");
        }}
        
        function updateView(metric) {{
            currentView = metric;
            updateTreemap();
        }}
        
        function formatSize(mb) {{
            if (mb >= 1000) return (mb / 1000).toFixed(1) + " GB";
            return mb + " MB";
        }}
        
        // Network functionality
        let networkInitialized = false;
        let network;
        
        function initNetwork() {{
            if (networkInitialized) return;
            networkInitialized = true;
            
            const container = document.getElementById('network');
            const data = {{
                nodes: new vis.DataSet(networkData.nodes),
                edges: new vis.DataSet(networkData.edges)
            }};
            
            const options = {{
                nodes: {{
                    shape: 'circle',
                    font: {{
                        color: '#F7FAFC',
                        size: 14,
                        face: 'Inter, system-ui, sans-serif'
                    }},
                    borderWidth: 2,
                    borderWidthSelected: 4,
                    scaling: {{
                        min: 20,
                        max: 50
                    }}
                }},
                edges: {{
                    color: {{
                        color: '#4A5568',
                        highlight: '#B794F4',
                        hover: '#B794F4'
                    }},
                    smooth: {{
                        type: 'continuous',
                        roundness: 0.5
                    }}
                }},
                physics: {{
                    forceAtlas2Based: {{
                        gravitationalConstant: -50,
                        centralGravity: 0.005,
                        springLength: 200,
                        springConstant: 0.05,
                        damping: 0.4
                    }},
                    solver: 'forceAtlas2Based',
                    stabilization: {{
                        iterations: 200
                    }}
                }},
                interaction: {{
                    hover: true,
                    tooltipDelay: 200,
                    hideEdgesOnDrag: true
                }}
            }};
            
            network = new vis.Network(container, data, options);
        }}
        
        // Initialize on load
        window.onload = function() {{
            initCharts();
        }};
    </script>
</body>
</html>"""

# ==============================================================================
# PURPOSE: MAIN PIPELINE ORCHESTRATOR
# AI_CONTEXT: Coordinates all modules to create the final visualization
# ==============================================================================

class SystemMapPipeline:
    """
    PURPOSE: Main pipeline class that orchestrates the entire process
    AI_CONTEXT: This is the main entry point - coordinates all modules
    """
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.scanner = FileSystemScanner(self.config)
        self.processor = DataProcessor(self.config)
        self.generator = HTMLGenerator(self.config)
        self.logger = logging.getLogger(__name__)
        
    def run(self, scan_path: str, output_path: str = None, max_depth: int = 3) -> str:
        """
        PURPOSE: Execute the complete system mapping pipeline
        AI_CONTEXT: Main method that runs all steps
        
        Args:
            scan_path: Root directory to scan
            output_path: Where to save HTML (defaults to scan_path/system_map.html)
            max_depth: Maximum directory depth to scan
            
        Returns:
            Path to generated HTML file
        """
        self.logger.info(f"Starting system map pipeline for {scan_path}")
        
        # Step 1: Scan file system
        self.logger.info("Step 1: Scanning file system...")
        scan_data = self.scanner.scan_directory(scan_path, max_depth)
        
        # Step 2: Process data
        self.logger.info("Step 2: Processing scan data...")
        processed_data = self.processor.process_scan_data(scan_data)
        
        # Step 3: Generate HTML
        self.logger.info("Step 3: Generating HTML visualization...")
        if output_path is None:
            output_path = os.path.join(scan_path, 'system_map.html')
            
        output_file = self.generator.generate_html(processed_data, output_path)
        
        self.logger.info(f"System map generated successfully: {output_file}")
        return output_file

# ==============================================================================
# PURPOSE: CLI INTERFACE
# AI_CONTEXT: Command-line interface for running the pipeline
# ==============================================================================

def main():
    """
    PURPOSE: Command-line interface for system map generation
    AI_CONTEXT: Parse arguments and run pipeline
    """
    parser = argparse.ArgumentParser(
        description='Generate interactive file system visualization',
        epilog='Example: python system_map.py ~ --output ~/Desktop/my_system_map.html'
    )
    
    parser.add_argument(
        'path',
        help='Root directory to scan (e.g., ~ or /Users/username)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output HTML file path (default: path/system_map.html)'
    )
    
    parser.add_argument(
        '--depth', '-d',
        type=int,
        default=3,
        help='Maximum directory depth to scan (default: 3)'
    )
    
    parser.add_argument(
        '--open',
        action='store_true',
        help='Open the generated HTML in browser'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Expand user path
    scan_path = os.path.expanduser(args.path)
    
    # Run pipeline
    try:
        pipeline = SystemMapPipeline()
        output_file = pipeline.run(scan_path, args.output, args.depth)
        
        print(f"✅ System map generated successfully!")
        print(f"📄 Output: {output_file}")
        
        # Open in browser if requested
        if args.open:
            subprocess.run(['open', output_file])
            print(f"🌐 Opened in browser")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1
        
    return 0

if __name__ == '__main__':
    exit(main())
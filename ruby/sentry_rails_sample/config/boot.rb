# Monkey-patch at_exit to track registration and execution order
module Kernel
  alias_method :original_at_exit, :at_exit

  @@at_exit_counter ||= 0

  def at_exit(&block)
    @@at_exit_counter += 1
    hook_id = @@at_exit_counter
    caller_info = caller(1..2).join("\n  ")

    # Capture worker/thread info at registration
    reg_pid = Process.pid
    reg_thread = Thread.current
    reg_thread_info = "#{reg_thread.object_id} (#{reg_thread.name || 'unnamed'})"

    puts "\n[REGISTERED ##{hook_id}] at_exit hook [PID: #{reg_pid}, Thread: #{reg_thread_info}]"
    puts "  #{caller_info}"

    original_at_exit do
      # Capture worker/thread info at execution
      exec_pid = Process.pid
      exec_thread = Thread.current
      exec_thread_info = "#{exec_thread.object_id} (#{exec_thread.name || 'unnamed'})"

      puts "\n[EXECUTING ##{hook_id}] at_exit hook [PID: #{exec_pid}, Thread: #{exec_thread_info}]"
      puts "  Originally from: #{caller_info}"
      puts "  Registered on: PID #{reg_pid}, Thread #{reg_thread_info}"
      block.call
    end
  end
end

ENV['BUNDLE_GEMFILE'] ||= File.expand_path('../Gemfile', __dir__)

require "bundler/setup" # Set up gems listed in the Gemfile.
require "bootsnap/setup" # Speed up boot time by caching expensive operations.
